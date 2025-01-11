import re
from pypdf import PdfReader
from keybert import KeyBERT




from sentence_transformers import SentenceTransformer




def extract_text_from_pdf(pdf_path):
    try:
        reader = PdfReader(pdf_path)
        number_of_pages = len(reader.pages)

        lines = []
        for i in range(number_of_pages):
            page = reader.pages[i]
            lines.append(page.extract_text().split("\n"))
        
        # Figure out a way to prune useless lines
        # Determine how relevant a line is to the document as a whole
        # For example, if a line is present in every page, it is probably not relevant
        # Using cosine similarity, we can determine how similar a line is to the rest of the document



        model = SentenceTransformer('all-MiniLM-L6-v2')
        # Generate sentence embeddings
        sentence_vectors = model.encode(lines)


        return '\n'.join(lines)

    except Exception as e:
        print(f"Error reading PDF file: {e}")
        return "ERROR"






text = extract_text_from_pdf("Antipode - 2010 - Alkon - Whiteness and Farmers Markets  Performances  Perpetuations     Contestations.pdf")  
# write text to a file

with open("text.txt", "w", encoding="utf-8") as file:
    file.write(text)
# print(text)








# text = "Often when beginners are tasked with writing a program to solve a problem, they jump immediately to writing code. Doesn’t matter whether the code is correct or not, or even if they fully understand the problem: somehow the allure of filling up the screen with text is too tempting. So before we go further in our study of the Python programming language, we’ll introduce the Function Design Recipe, a structured process for taking a problem description and designing and implementing a function in Python to solve this problem."
kw_model = KeyBERT()
keywords = kw_model.extract_keywords(text, keyphrase_ngram_range=(1, 2), stop_words='english')

print(keywords)






# how to do the checklist thing??
# fine tune for specific subjects?????????????
# for math: look for theorems that are important, how these theorems can be used, etc
# for programming: look for important functions, how they can be used, etc
# if the text is for example: 
# "The derivative of a function is the slope of the tangent line to the graph of the function at a point. The derivative of a function at a point is the limit of the average rate of change of the function over a small interval containing the point as the interval approaches zero."
# the main ideas that need to be extracted are:
# - derivative of a function is the slope of the tangent line to the graph of the function at a point
# - derivative of a function at a point is the limit of the average rate of change of the function over a small interval containing the point as the interval approaches zero





# important definitions - can be extracted by keybert
# important concepts
# important theorems
# examples


# how to use these things
