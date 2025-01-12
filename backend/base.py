from flask import Flask, request, jsonify, send_file
from openai import OpenAI
from flask_cors import CORS
from werkzeug.utils import secure_filename
from flask_sqlalchemy import SQLAlchemy
import os
import numpy as np
from sklearn.cluster import KMeans
from nltk import tokenize
from pypdf import PdfReader
from rake_nltk import Rake
import math
import nltk

# Download required NLTK data
nltk.download('punkt')
nltk.download('stopwords')

app = Flask(__name__)
CORS(app)

# Database setup
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///mydatabase.db"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
db = SQLAlchemy(app)

OPENAI_API_KEY = "key"

class Transcription(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    transcription = db.Column(db.String(10000), unique=False, nullable=False)

# PDF Processing Functions
def vectorize_sentences(sentences):
    client = OpenAI(api_key=OPENAI_API_KEY)
    embeddings = []
    for sentence in sentences:
        response = client.embeddings.create(
            model="text-embedding-ada-002",
            input=sentence
        )
        embeddings.append(response.data[0].embedding)
    return np.array(embeddings)

def kmeans_clustering(sentences, sentence_vectors):
    num_clusters = min(max(len(sentences) // 5, 1), 20)
    kmeans = KMeans(n_clusters=num_clusters, random_state=42)
    kmeans.fit(sentence_vectors)
    cluster_labels = kmeans.labels_
    
    clusters = {}
    for sentence, label in zip(sentences, cluster_labels):
        clusters.setdefault(label, []).append(sentence)
    
    for cluster in list(clusters.keys()):
        if len(clusters[cluster]) <= 2:
            del clusters[cluster]
    
    return clusters

def rank_sentences(sentences, sentence_vectors):
    mean_vector = sentence_vectors.mean(axis=0)
    similarities = sentence_vectors @ mean_vector / (np.linalg.norm(sentence_vectors, axis=1) * np.linalg.norm(mean_vector))
    ranked_sentences = [sentence.replace('\n', '') for _, sentence in sorted(zip(similarities, sentences), reverse=True)]
    return ranked_sentences

def parse_text_from_pdf(pdf_path):
    reader = PdfReader(pdf_path)
    pages = [page.extract_text() for page in reader.pages]
    text = ' '.join(pages)
    
    sentences = tokenize.sent_tokenize(text)
    sentences = rank_sentences(sentences, vectorize_sentences(sentences))[:len(sentences)//1]
    sentence_vectors = vectorize_sentences(sentences)
    clusters = kmeans_clustering(sentences, sentence_vectors)
    return clusters

# Audio Processing Functions
def interpret_mp3(file):
    client = OpenAI(api_key=OPENAI_API_KEY)
    audio_file = open(file, "rb")
    transcription = client.audio.transcriptions.create(
        model="whisper-1",
        file=audio_file
    )
    audio_file.close()
    return transcription.text

def extract_keywords(text):
    rake = Rake()
    rake.extract_keywords_from_text(text)
    keywords = rake.get_ranked_phrases()
    word = ""
    for i in range(len(keywords) - 1):
        word += keywords[i] + ","
    if len(keywords) != 0:
        word += keywords[-1]
    return word

def name_cluster(sentences):
    client = OpenAI(api_key=OPENAI_API_KEY)
    prompt = f"Name the following cluster of sentences: {sentences}"
    completion = client.chat.completions.create(
        model="gpt-4",
        messages=[
            {"role": "system", "content": "You are a helpful assistant."},
            {"role": "user", "content": prompt}
        ]
    )
    return completion.choices[0].message.content

def cosine_similarity(v1, v2):
    return np.dot(v1, v2) / (np.linalg.norm(v1) * np.linalg.norm(v2))

def compare_text_to_audio(sentences, transcription):
    vector = vectorize_sentences([transcription])[0]
    sentence_vectors = vectorize_sentences(sentences)
    similarities = []
    
    average_similarity = 0
    for sentence_vector in sentence_vectors:
        average_similarity += cosine_similarity(vector, sentence_vector)
    average_similarity /= len(sentence_vectors)
    return average_similarity

# Routes
@app.route('/upload_audio', methods=['POST'])
def upload_audio():
    if 'audio' not in request.files:
        return jsonify({'error': 'No audio file part'}), 400

    audio_file = request.files['audio']
    if audio_file.filename == '':
        return jsonify({'error': 'No selected file'}), 400

    audio_path = 'uploaded_audio.wav'
    audio_file.save(audio_path)
    return jsonify({'audio_url': f'http://localhost:5000/{audio_path}'})

@app.route('/transcribe', methods=['GET'])
def transcribe_audio():
    try:
        client = OpenAI(api_key=OPENAI_API_KEY)

        audio_file = open("uploaded_audio.wav", "rb")
        transcription = client.audio.transcriptions.create(
            model="whisper-1", 
            file=audio_file
        )
        
        # Save transcription to database
        new_transcription = Transcription(transcription=transcription.text)
        db.session.add(new_transcription)
        db.session.commit()
        
        # Call calcresults with the transcription
        return calcresults(transcription.text, new_transcription.id)
        
    except Exception as e:
        print(f"Error in transcribe: {str(e)}")
        return jsonify({"error": str(e)}), 500
    finally:
        if 'audio_file' in locals():
            audio_file.close()

def calcresults(transcription_text, transcription_id):
    try:
        # Extract keywords
        keywords = extract_keywords(transcription_text)
        
        # Compare with PDF if available
        results = {}
        pdf_filename = request.args.get('pdfFileName')  # Get from query params
        if pdf_filename:
            pdf_path = os.path.join('fileuploads', pdf_filename)
            if os.path.exists(pdf_path):
                clusters = parse_text_from_pdf(pdf_path)
                for cluster_id, sentences in clusters.items():
                    results[cluster_id] = compare_text_to_audio(sentences, transcription_text)
        
        response = jsonify({
            "transcription": transcription_text,
            "id": transcription_id,
            "keywords": keywords,
            "cluster_results": results
        })
        
        #response.headers.add('Access-Control-Allow-Origin', '*')
        return response, 200
        
    except Exception as e:
        print(f"Error: {str(e)}")
        return jsonify({"error": str(e)}), 500

@app.route('/uploaded_audio.wav')
def serve_audio():
    return send_file('uploaded_audio.wav', mimetype='audio/wav')

# PDF Upload Configuration
UPLOAD_FOLDER = 'fileuploads'
ALLOWED_EXTENSIONS = {'pdf'}

if not os.path.exists(UPLOAD_FOLDER):
    os.makedirs(UPLOAD_FOLDER)

app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

@app.route('/upload_pdf', methods=['POST'])
def upload_file():
    if 'file' not in request.files:
        return jsonify({'error': 'No file part'}), 400
    
    file = request.files['file']
    if file.filename == '':
        return jsonify({'error': 'No selected file'}), 400
    
    if file and allowed_file(file.filename):
        filename = secure_filename(file.filename)
        file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
        return jsonify({'message': 'File uploaded successfully'}), 200
    
    return jsonify({'error': 'File type not allowed'}), 400

@app.route('/api/receive_string', methods=['POST'])
def receive_string():
    try:
        data = request.get_json()
        print("Received data:", data)  # Debug log
        
        transcription = data.get('transcription')
        pdf_filename = data.get('pdfFileName')
        
        if not transcription:
            return jsonify({"error": "No transcription provided"}), 400
        if not pdf_filename:
            return jsonify({"error": "No PDF filename provided"}), 400

        # Get PDF clusters
        pdf_path = os.path.join('fileuploads', pdf_filename)
        print(f"Processing PDF: {pdf_path}")  # Debug log
        
        if not os.path.exists(pdf_path):
            return jsonify({"error": f"PDF not found: {pdf_path}"}), 404

        results = 0
        resultscount = 0
        coverage_count = 0
        total_clusters = 0
        
        # Get clusters and convert numpy.int32 keys to regular integers
        clusters = parse_text_from_pdf(pdf_path)
        converted_clusters = {int(k): v for k, v in clusters.items()}
        
        for cluster_id, sentences in converted_clusters.items():
            results += compare_text_to_audio(sentences, transcription)
            resultscount += 1
            #results[str(cluster_id)] = {
           #     "covered": bool(result),
           #     "sentences": sentences
           # }
            #if result:
            #    coverage_count += 1
            #total_clusters += 1

        # Calculate coverage
        coverage_percentage = (results / resultscount) * 100

        response_data = {
            "coverage_percentage": float(coverage_percentage),
            "cluster_results": results
        }
        
        print("Sending response:", response_data)
        return jsonify(response_data), 200

    except Exception as e:
        print(f"Error in receive_string: {str(e)}")
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(debug=True)