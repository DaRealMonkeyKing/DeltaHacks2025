import re
from pypdf import PdfReader
from sklearn.cluster import KMeans
from blingfire import text_to_sentences
from sentence_transformers import SentenceTransformer
from sklearn.metrics.pairwise import cosine_similarity as cs


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

    # Delete clusters that are almost perfectly similar to themselves
    for cluster in list(clusters.keys()):
        check_delete_cluster(clusters, cluster)

    # Preview clusters
    for cluster, cluster_sentences in clusters.items():
        print(f"Cluster {cluster}:")
        for sentence in cluster_sentences[:10]:
            print(f"  - {sentence}")

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
    sentences = text_to_sentences(text).split('\n')

    # example test sentences
    # sentences = ["The quick brown fox jumps over the lazy dog.",
    #              "A journey of a thousand miles begins with a single step.",
    #              "To be or not to be, that is the question.",
    #              "All that glitters is not gold.",
    #              "The only thing we have to fear is fear itself.",
    #              "I think, therefore I am.",
    #              "The unexamined life is not worth living.",
    #              "To infinity and beyond!",
    #              "May the Force be with you.",
    #              "Elementary, my dear Watson."]

    sentences = rank_sentences(sentences, vectorize_sentences(sentences))[:len(sentences)//4]
    
    # Generate sentence vectors for the modified sentences
    sentence_vectors = vectorize_sentences(sentences)

    # Cluster sentences
    clusters = kmeans_clustering(sentences, sentence_vectors)

    return clusters


def check_delete_cluster(clusters, cluster_number):
    # if a cluster is almost perfectly similar to itself and has a lot of sentences, it is likely to be a duplicate
    # and delete
    cluster_sentences = clusters[cluster_number]
    if len(cluster_sentences) > 1:
        vectors = vectorize_sentences(cluster_sentences)
        similarity_matrix = cs(vectors)
        avg_similarity = similarity_matrix.mean()

        print(cluster_sentences, avg_similarity)
        if avg_similarity > 0.8:  # Threshold for similarity
            del clusters[cluster_number]


def rank_sentences(sentences, sentence_vectors):
    # Compute cosine similarity between each sentence and the mean vector
    mean_vector = sentence_vectors.mean(axis=0)
    similarities = sentence_vectors @ mean_vector

    # Rank sentences by similarity score
    ranked_sentences = [sentence for _, sentence in sorted(zip(similarities, sentences), reverse=True)]
    return ranked_sentences




# text = extract_text_from_pdf("fileuploads/Antipode - 2010 - Alkon - Whiteness and Farmers Markets  Performances  Perpetuations     Contestations.pdf")
# text = extract_text_from_pdf("fileuploads/a08.pdf")
# text = extract_text_from_pdf("fileuploads/LectureNotes.pdf")
points = parse_text_from_pdf("fileuploads/Is Elon Musk The Greatest Leader On Earth_.pdf")
