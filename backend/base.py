from flask import Flask, request, jsonify, send_file
import os

app = Flask(__name__)

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


if __name__ == '__main__':
    app.run(debug=True)