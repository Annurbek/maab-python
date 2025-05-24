#Word Frequency Counter
import os
import string
from collections import Counter

def get_text():
    if not os.path.exists("lesson-6/homework/sample.txt"):
        print("sample.txt does not exist. Please enter text to create it.")
        text = input("Enter your paragraph: ")
        with open("lesson-6/homework/sample.txt", "w") as file:
            file.write(text)
    with open("lesson-6/homework/sample.txt", "r") as file:
        return file.read()

def clean_text(text):
    text = text.lower()  # Convert to lowercase
    text = text.translate(str.maketrans('', '', string.punctuation))  # Remove punctuation
    words = text.split()  # Split into words
    return words

def count_words(words):
    return Counter(words)  # Count word occurrences

def display_results(word_counts, top_n=5):
    total_words = sum(word_counts.values())
    print(f"Total words: {total_words}")
    print("Top", top_n, "most common words:")
    for word, count in word_counts.most_common(top_n):
        print(f"{word} - {count} times")

def save_results(word_counts, total_words, top_n=5):
    with open("lesson-6/homework/word_count_report.txt", "w") as file:
        file.write("Word Count Report\n")
        file.write(f"Total Words: {total_words}\n")
        file.write("Top 5 Words:\n")
        for word, count in word_counts.most_common(top_n):
            file.write(f"{word} - {count}\n")
    print("Results saved to word_count_report.txt")

def main():
    text = get_text()
    words = clean_text(text)
    word_counts = count_words(words)
    total_words = sum(word_counts.values())
    
    try:
        top_n = int(input("Enter the number of top common words to display: "))
    except ValueError:
        top_n = 5  # Default to 5 if invalid input
    
    
    display_results(word_counts, top_n)
    save_results(word_counts, total_words, top_n)

if __name__ == "__main__":
    main()