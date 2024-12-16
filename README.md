Plagiarism Checker 📄🔍

This project is a simple yet effective plagiarism detection tool that compares the content of two text files and calculates their similarity using TF-IDF (Term Frequency-Inverse Document Frequency) and Cosine Similarity. The tool identifies potential plagiarism by analyzing the textual content of the files.

🚀 Features

Text Similarity Analysis: Detects the level of similarity between two documents.
Interactive Command-Line Interface: Users can input file paths directly via the terminal.
Efficient and Accurate: Uses the TF-IDF vectorization technique combined with Cosine Similarity for precise comparisons.
Plagiarism Alerts: Warns users if the similarity score exceeds a threshold (e.g., 75%).

📂 Project Structure

plagiarism_checker.py: Main script containing the functionality to read files, compute similarity, and display results.

🛠️ Technologies Used

Python: Core programming language.
Scikit-learn: Library for implementing TF-IDF vectorization and Cosine Similarity.

📊 How It Works

File Input: Users provide paths to two text files for comparison.
TF-IDF Vectorization: Converts textual data into numerical vectors based on term frequency and inverse document frequency.
Cosine Similarity: Measures the cosine of the angle between two vectors to determine their similarity.
Output: Displays the similarity score and provides a warning if plagiarism is suspected.
