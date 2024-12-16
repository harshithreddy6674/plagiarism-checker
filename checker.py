from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

def read_file(file_path):
    """Reads the content of a file and returns it as a string."""
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            return file.read()
    except FileNotFoundError:
        print(f"Error: File not found - {file_path}")
        return None

def calculate_similarity(doc1, doc2):
    """Calculates and returns the cosine similarity between two documents."""
    vectorizer = TfidfVectorizer()
    tfidf_matrix = vectorizer.fit_transform([doc1, doc2])
    similarity = cosine_similarity(tfidf_matrix[0:1], tfidf_matrix[1:2])
    return similarity[0][0] * 100

def main():
    # Input file paths
    file1_path = input("Enter the path to the first file: ")
    file2_path = input("Enter the path to the second file: ")

    # Read files
    doc1 = read_file(file1_path)
    doc2 = read_file(file2_path)

    if doc1 is not None and doc2 is not None:
        # Calculate similarity
        similarity_score = calculate_similarity(doc1, doc2)
        print(f"\nSimilarity Score: {similarity_score:.2f}%")
        if similarity_score > 75:
            print("Warning: High similarity detected. Possible plagiarism.")
        else:
            print("Low similarity. Documents are likely unique.")

if __name__ == "__main__":
    main()
