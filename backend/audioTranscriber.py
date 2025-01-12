from openai import OpenAI
import os
import math
import numpy as np
from rake_nltk import Rake
import nltk
from pdf_parser import parse_text_from_pdf, vectorize_sentences


nltk.download('punkt')
nltk.download('stopwords')




print(os.getenv("OPENAI_KEY1"))
print(os.getenv("OPENAI_KEY2"))


def interpret_mp3(file):
    client = OpenAI(api_key=os.getenv("OPENAI_KEY1"))
    audio_file= open(file, "rb")
    transcription = client.audio.transcriptions.create(
        model="whisper-1",
        file=audio_file
    )


    print(transcription.text)
    return transcription.text






def extract_keywords(text):
    rake = Rake()
    rake.extract_keywords_from_text(text)
    keywords = rake.get_ranked_phrases() # ranks phrases based on importance
    word = ""
    for i in range(len(keywords) - 1):
        word += keywords[i] + ","


    if len(keywords) != 0:
        word += keywords[-1]
    #print(keywords)
    return word










def name_cluster(sentences):
    prompt = f"""Name the following cluster of sentences:"""
    print(os.getenv("OPENAI_KEY2"))
    client = OpenAI(api_key=os.getenv("OPENAI_KEY2"))
    completion = client.chat.completions.create(
        model="gpt-4o",
        messages=[{"role": "system", "content": "You are a helpful assistant."},{"role": "user", "content": prompt}])
    return completion.choices[0].message.content






def compare_text_to_audio(sentences):
    #spokenSentence = interpret_mp3("AudioTests/audioTest.mp3")
    vector = vectorize_sentences(["Today I lost to Niel Yang in chess. I got brutally checkmated in the worst way possible."])[0]
    sentence_vectors = vectorize_sentences(sentences)
    similarities = []


    average_similarity = 0
    for sentence_vector in sentence_vectors:
        average_similarity += cosine_similarity(vector,sentence_vector)
    average_similarity /= len(sentence_vectors)
    if average_similarity > 0.5:
        return True
    return False
   


def cosine_similarity(v1, v2):
    return np.dot(v1, v2) / (np.linalg.norm(v1) * np.linalg.norm(v2))




pdf = "fileuploads/The-Paper-Menagerie+By+Ken+Liu.pdf"
clusters = parse_text_from_pdf(pdf)
for cluster, sentences in clusters.items():
    if compare_text_to_audio(sentences):
        print("YAY")
    else:
        print("NAY", sentences)




t = "Elon Musk: an extraordinary leader. All the leaders that I researched for my book are extraordinary businesspeople."
s = "Ryan's Shoes"
#print(extract_keywords(t))
#print(extract_keywords(s))
print(compare_text_to_audio(t))
#spoken_words = interpret_mp3("backend/AudioTests/audioTest.mp3")
#extract_keywords(spoken_words)

