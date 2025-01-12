from openai import OpenAI
import os
from rake_nltk import Rake
import nltk

#nltk.download('punkt_tab')
#nltk.download('stopwords')

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





def compare_text_to_audio(text, spoken):
    text_keywords = extract_keywords(text)
    spoken_keywords = extract_keywords(spoken)

    prompt = f"""- List words in the list [{text_keywords}] that are not in the list of words [{spoken_keywords}] 
            - If the main ideas that were spoken do not match the text, list the missed ideas
            - Don't add additional comments at the end
            - Don't include anything that is not in the original text
            - If no important idea was missed, return an empty string"""
    print(os.getenv("OPENAI_KEY2"))
    client = OpenAI(api_key=os.getenv("OPENAI_KEY2"))
    completion = client.chat.completions.create(
        model="gpt-4o",
        messages=[{"role": "system", "content": "You are a helpful assistant."},{"role": "user", "content": prompt}])
    return completion.choices[0].message.content

t = "Elon Musk: an extraordinary leader. All the leaders that I researched for my book are extraordinary businesspeople."
s = "Ryan's Shoes"
#print(extract_keywords(t))
#print(extract_keywords(s))
print(compare_text_to_audio(t,s))
#spoken_words = interpret_mp3("backend/AudioTests/audioTest.mp3")
#extract_keywords(spoken_words)