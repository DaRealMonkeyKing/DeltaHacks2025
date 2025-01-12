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
    client = OpenAI(api_key=os.getenv("OPENAI_KEY1"))
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
    client = OpenAI(api_key=os.getenv("OPENAI_KEY2"))
    completion = client.chat.completions.create(
        model="gpt-4o",
        messages=[{"role": "system", "content": "You are a helpful assistant."},{"role": "user", "content": prompt}])
    return completion.choices[0].message.content


def compare_text_to_audio(sentences):
    #spokenSentence = interpret_mp3("AudioTests/audioTest.mp3")
    story = """
Jack’s mother could bring paper to life. As a child, Jack was fascinated by the paper animals she folded—tigers that prowled, cranes that flapped their wings, and whales that swam through the air. His favorite was a small paper tiger named Laohu, who purred against his cheek when he was sad and wrestled with his action figures when he was happy. The magic his mother wove into these creations felt as natural as breathing. 

But as Jack grew older, things changed. He began to notice the differences between himself and the other kids in their suburban American neighborhood. His classmates teased him about his mother’s broken English and their Chinese food at home. They didn’t understand the strange magic of the paper animals; they called it weird. Wanting desperately to fit in, Jack pushed away the parts of himself that felt foreign—his mother, her traditions, and the magical animals she made.

By the time Jack was in high school, he no longer spoke Chinese, and the paper animals lay forgotten in a box. He didn’t even try to defend his mother when his classmates mocked her. It was easier that way.

Years later, after Jack’s mother passed away, he stumbled upon the old box of paper animals while sorting through her belongings. They were worn and faded, reminders of a childhood he had long buried. Laohu, the little paper tiger, seemed especially fragile. When Jack picked him up, the tiger stirred weakly, and Jack noticed faint writing on the inside of the paper.

Carefully unfolding Laohu, Jack found a letter his mother had written in Chinese. She poured out her heart, recounting her life in China, her painful journey to America, and the sacrifices she made to raise him in a better world. She explained how much she had loved him, even when he turned away from her, and how proud she was of him despite the distance between them.

Reading the letter, Jack felt the weight of her love and the regret of all the moments he had dismissed her, moments he could never get back. Tears streamed down his face as he realized what he had lost—her language, her culture, and her magic—now gone forever.

Holding the faded paper tiger close, Jack finally understood that the magic was never just in the animals. It was in the love his mother had poured into every fold, every crease. And it had always been with him, waiting for him to see it.
"""
    story = "My name is WILLLIAM LIU. AND I AM CHINESE. I POURED OUT MY HEART TO MY SON JACK."
    # story = extract_keywords(story)
    vector = vectorize_sentences([story])[0]

    # sentence_vectors = vectorize_sentences([extract_keywords(sentence) for sentence in sentences])
    sentence_vectors = vectorize_sentences(sentences)
    similarities = []


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

