from flask import Flask, request, jsonify, send_file
import os
from openai import OpenAI
from flask_cors import CORS
from werkzeug.utils import secure_filename

app = Flask(__name__)
CORS(app, resources={
    r"/*": {
        "origins": ["http://localhost:5174", "http://127.0.0.1:5174"],
        "methods": ["GET", "POST", "OPTIONS"],
        "allow_headers": ["Content-Type", "Authorization", "Access-Control-Allow-Origin"],
        "supports_credentials": True
    }
})


@app.route('/upload_audio', methods=['POST'])
def upload_audio():
    if 'audio' not in request.files:
        return jsonify({'error': 'No audio file part'}), 400

    audio_file = request.files['audio']
    if audio_file.filename == '':
        return jsonify({'error': 'No selected file'}), 400

    # Save the uploaded audio file temporarily
    audio_path = 'uploaded_audio.wav'
    audio_file.save(audio_path)

    # Return the WAV file URL (or serve the file directly)
    return jsonify({'audio_url': f'http://localhost:5000/{audio_path}'})


@app.route('/uploaded_audio.wav')
def serve_audio():
    return send_file('uploaded_audio.wav', mimetype='audio/wav')


@app.route('/transcribe', methods=['GET'])
def transcribe_audio():
    client = OpenAI(api_key="API_KEY")

    audio_file= open("uploaded_audio.wav", "rb")
    transcription = client.audio.transcriptions.create(
        model="whisper-1", 
        file=audio_file
    )
    print(transcription.text)
    return jsonify({"transcription": transcription.text}), 200


# Configure upload folder
UPLOAD_FOLDER = 'fileuploads'
ALLOWED_EXTENSIONS = {'pdf'}

# Create upload folder if it doesn't exist
if not os.path.exists(UPLOAD_FOLDER):
    os.makedirs(UPLOAD_FOLDER)

app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

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


if __name__ == '__main__':
    app.run(debug=True)