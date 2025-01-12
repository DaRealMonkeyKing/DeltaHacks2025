from openai import OpenAI
import os
import math
import numpy as np
from rake_nltk import Rake
import nltk
from pdf_parser import parse_text_from_pdf, vectorize_sentences


nltk.download('punkt')
nltk.download('stopwords')


def interpret_mp3(file):
    #client = OpenAI()
    audio_file= open(file, "rb")
    transcription = client.audio.transcriptions.create(
        model="whisper-1",
        file=audio_file
    )
    return transcription.text


def extract_keywords(text):
    rake = Rake()
    rake.extract_keywords_from_text(text)
    keywords = rake.get_ranked_phrases() # ranks phrases based on importance
    word = ""
    for i in range(len(keywords) - 1):
        word += keywords[i] + " "


    if len(keywords) != 0:
        word += keywords[-1]
    return word


def name_cluster(sentences):
    prompt = f"""Give a name the following cluster of sentences: {sentences}"""
    #client = OpenAI()
    completion = client.chat.completions.create(
        model="gpt-4o",
        messages=[{"role": "system", "content": "You are a helpful assistant."},{"role": "user", "content": prompt}])
    return completion.choices[0].message.content


def compare_text_to_audio(sentences, filepath):
    spokenSentence = interpret_mp3(filepath)

    # story = extract_keywords(story)
    vector = vectorize_sentences([spokenSentence])[0]

    # sentence_vectors = vectorize_sentences([extract_keywords(sentence) for sentence in sentences])
    sentence_vectors = vectorize_sentences(sentences)

    average_similarity = 0
    for sentence_vector in sentence_vectors:
        average_similarity += cosine_similarity(vector,sentence_vector)
        
    return average_similarity / len(sentence_vectors)
   


def cosine_similarity(v1, v2):
    # print(np.dot(v1, v2) / (np.linalg.norm(v1) * np.linalg.norm(v2)), v1, v2)
    return np.dot(v1, v2) / max(np.linalg.norm(v1) * np.linalg.norm(v2), 0.000000001)




pdf = "fileuploads/The-Paper-Menagerie+By+Ken+Liu.pdf"
clusters = parse_text_from_pdf(pdf)
for cluster, sentences in clusters.items():
    if (score:=compare_text_to_audio(sentences)) > 0.25:
        print(f'YAY: {name_cluster(sentences)}')
    else:
        print(f'NAY: {name_cluster(sentences)}')
    print('COMPREHENSION PERCENT: ', max(min(score*250, 100), 0))




#spoken_words = interpret_mp3("backend/AudioTests/audioTest.mp3")
#extract_keywords(spoken_words)

