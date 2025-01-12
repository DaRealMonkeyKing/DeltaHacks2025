from openai import OpenAI
import os

def interpret_mp3(file):
    client = OpenAI(api_key=os.getenv("OPENAI_KEY"))
    audio_file= open(file, "rb")
    transcription = client.audio.transcriptions.create(
        model="whisper-1", 
        file=audio_file
    )

    print(transcription.text)

interpret_mp3("backend/AudioTests/audioTest.mp3")