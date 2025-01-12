import re
from pypdf import PdfReader
from sklearn.cluster import KMeans
from blingfire import text_to_sentences
from sentence_transformers import SentenceTransformer


def vectorize_sentences(sentences):
    model = SentenceTransformer('all-MiniLM-L6-v2')
    # Generate sentence embeddings
    sentence_vectors = model.encode(sentences)
    return sentence_vectors


def kmeans_clustering(sentences, sentence_vectors):
    # Set the number of clusters (k) based on your dataset
    num_clusters = 20

    # Fit K-Means
    kmeans = KMeans(n_clusters=num_clusters, random_state=42)
    kmeans.fit(sentence_vectors)

    # Get cluster assignments
    cluster_labels = kmeans.labels_

    # Group sentences by their cluster
    clusters = {}
    for sentence, label in zip(sentences, cluster_labels):
        clusters.setdefault(label, []).append(sentence)

    # Preview clusters
    for cluster, cluster_sentences in clusters.items():
        print(f"Cluster {cluster}:")
        for sentence in cluster_sentences[:10]:
            print(f"  - {sentence}")

    return clusters


def extract_text_from_pdf(pdf_path):
    reader = PdfReader(pdf_path)
    number_of_pages = len(reader.pages)

    sentences = []
    pages = []
    for i in range(number_of_pages):
        page = reader.pages[i]
        pages.append(page.extract_text())
    text = ' '.join(pages)
    sentences = text_to_sentences(text).split('\n')

    sentence_vectors = vectorize_sentences(sentences)
    clusters = kmeans_clustering(sentences, sentence_vectors)

    return '\n'.join(sentences)


text = extract_text_from_pdf("Antipode - 2010 - Alkon - Whiteness and Farmers Markets  Performances  Perpetuations     Contestations.pdf")
# text = extract_text_from_pdf("LectureNotes.pdf")