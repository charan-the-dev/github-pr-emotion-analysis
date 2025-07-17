import pandas as pd
import re
import string
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer
from nltk.tokenize import word_tokenize
import nltk
import sqlite3
import os
from store import getAllComments

# Download NLTK resources if not already
nltk.download('punkt')
nltk.download('stopwords')
nltk.download('wordnet')

# Example: loading data
# df = pd.read_csv('your_data.csv')
# Assuming you have a 'text' column
# Initialize the Database

df = getAllComments("./data/comments.db")

print(df.columns)

def preprocess_text(text):
    # Lowercase
    text = text.lower()
    
    # Remove URLs
    text = re.sub(r'http\S+|www\S+|https\S+', '', text, flags=re.MULTILINE)
    
    # Remove mentions and hashtags
    text = re.sub(r'\@\w+|\#','', text)
    
    # Remove punctuation
    text = text.translate(str.maketrans('', '', string.punctuation))
    
    # Remove numbers
    text = re.sub(r'\d+', '', text)
    
    # Tokenization
    tokens = word_tokenize(text)
    
    # Remove stopwords and lemmatize
    tokens = [lemmatizer.lemmatize(word) for word in tokens if word not in stop_words]
    
    # Join tokens back to string
    return ' '.join(tokens)

# Apply preprocessing
# df['clean_text'] = df['text'].apply(preprocess_text)

# # # View processed data
# print(df[['text', 'clean_text']].head())

conn.close()
