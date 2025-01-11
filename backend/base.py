from flask import Flask, request, jsonify, send_file
import os
from openai import OpenAI
from flask import Flask, jsonify
from flask_cors import CORS


app = Flask(__name__)
CORS(app)

@app.route('/upload', methods=['POST'])
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
    client = OpenAI(api_key="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")

    audio_file= open("uploaded_audio.wav", "rb")
    transcription = client.audio.transcriptions.create(
        model="whisper-1", 
        file=audio_file
    )
    print(transcription.text)
    return jsonify({"transcription": transcription.text}), 200

if __name__ == '__main__':
    app.run(debug=True)