import re
import nltk
from nltk.tokenize import sent_tokenize, word_tokenize
from nltk.corpus import stopwords
from collections import defaultdict
from heapq import nlargest

# Ensure necessary NLTK data is downloaded
nltk.download('punkt')
nltk.download('stopwords')

def summarize_text(text, num_sentences=3):
    """ 
    Generates an extractive summary of a text after preprocessing. 
    Args: 
        text (str): The input text paragraph. 
        num_sentences (int): The desired number of sentences in the summary. 
    Returns: 
        str: The generated extractive summary. 
    """

    # Step 1: Preprocess the text to remove special characters and digits
    cleaned_text = re.sub(r'[^a-zA-Z\s.]', '', text, re.I|re.A)
    cleaned_text = re.sub(r'\s+', ' ', cleaned_text).strip()

    # Handle cases where all text is removed
    if not cleaned_text or cleaned_text.isspace():
        return "Not enough text to generate a summary."

    # Tokenize the text into sentences
    sentences = sent_tokenize(cleaned_text, language='english')
    if len(sentences) <= num_sentences:
        return cleaned_text  # Return original text if it's already short

    # Tokenize the text into words and remove stopwords
    stop_words = set(stopwords.words('english'))
    word_frequencies = defaultdict(int)
    for word in word_tokenize(cleaned_text):
        if word.lower() not in stop_words and word.isalpha():
            word_frequencies[word.lower()] += 1

    # Check if word_frequencies is empty
    if not word_frequencies:
        return "Not enough meaningful words to generate a summary."

    # Normalize the word frequencies
    max_frequency = max(word_frequencies.values())
    for word in word_frequencies.keys():
        word_frequencies[word] = word_frequencies[word] / max_frequency

    # Step 2: Score sentences based on word frequency
    sentence_scores = defaultdict(int)
    for sentence in sentences:
        for word in word_tokenize(sentence):
            if word.lower() in word_frequencies:
                sentence_scores[sentence] += word_frequencies[word.lower()]

    # Step 3: Extract the top N sentences for the summary
    summary_sentences = nlargest(num_sentences, sentence_scores, key=sentence_scores.get)

    # Join the sentences to form the summary
    summary = ' '.join(summary_sentences)
    return summary

# Example usage with a sample paragraph
sample_paragraph = """ 
Artificial intelligence (AI) is a rapidly advancing field of computer science. 
Its applications range from simple chatbots to complex autonomous vehicles. 
AI systems are designed to perform tasks that would normally require human intelligence, 
such as visual perception, speech recognition, and decision-making. 
In recent years, the development of deep learning models has significantly boosted AI's 
capabilities, leading to major breakthroughs. 
The ethical implications of AI, however, are a subject of ongoing debate. Some researchers 
believe AI could solve some of the world's most complex problems. 
While others worry about its potential impact on employment and data privacy. 
The future of AI holds great promise and many challenges, with billions of dollars being 
invested in research and development each year. 
"""

# Generate a summary with 3 sentences
generated_summary = summarize_text(sample_paragraph, num_sentences=3)
print("Original Text:")
print(sample_paragraph)
print("\n--- Extractive Summary ---")
print(generated_summary)
