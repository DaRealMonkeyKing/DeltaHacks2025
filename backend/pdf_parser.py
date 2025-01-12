import re
from pypdf import PdfReader
from sklearn.cluster import KMeans
from nltk import tokenize
from sentence_transformers import SentenceTransformer








def vectorize_sentences(sentences):
    model = SentenceTransformer('all-MiniLM-L6-v2')
    # Generate sentence embeddings
    sentence_vectors = model.encode(sentences)
    return sentence_vectors




def kmeans_clustering(sentences, sentence_vectors):
    # Set the number of clusters (k) based on your dataset
    num_clusters = min(max(len(sentences) // 5, 1), 20)


    # Fit K-Means
    kmeans = KMeans(n_clusters=num_clusters, random_state=42)
    kmeans.fit(sentence_vectors)


    # Get cluster assignments
    cluster_labels = kmeans.labels_


    # Group sentences by their cluster
    clusters = {}
    for sentence, label in zip(sentences, cluster_labels):
        clusters.setdefault(label, []).append(sentence)


    for cluster in list(clusters.keys()):
        check_delete_cluster(clusters, cluster)


    return clusters




def parse_text_from_pdf(pdf_path):
    reader = PdfReader(pdf_path)
    number_of_pages = len(reader.pages)


    sentences = []
    pages = []
    for i in range(number_of_pages):
        page = reader.pages[i]
        pages.append(page.extract_text())
    text = ' '.join(pages)




    # NOTE: VERY EXPENSIVE OPERATIONS
    sentences = tokenize.sent_tokenize(text)
    sentences = rank_sentences(sentences, vectorize_sentences(sentences))[:len(sentences)//4]
   
    # Generate sentence vectors for the modified sentences
    sentence_vectors = vectorize_sentences(sentences)


    # Cluster sentences
    clusters = kmeans_clustering(sentences, sentence_vectors)


    return clusters




def check_delete_cluster(clusters, cluster_number):
    cluster_sentences = clusters[cluster_number]
    if len(cluster_sentences) <= 2:
        del clusters[cluster_number]




# Optimize this
def rank_sentences(sentences, sentence_vectors):
    # Compute cosine similarity between each sentence and the mean vector
    mean_vector = sentence_vectors.mean(axis=0)
    similarities = sentence_vectors @ mean_vector / (np.linalg.norm(sentence_vectors, axis=1) * np.linalg.norm(mean_vector))


    # Rank sentences by similarity score
    ranked_sentences = [sentence.replace('\n', '') for _, sentence in sorted(zip(similarities, sentences), reverse=True)]
    return ranked_sentences


