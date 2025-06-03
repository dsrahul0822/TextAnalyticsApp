# utils/preprocessing.py

import re
import nltk
import os

# Setup for Streamlit Cloud compatibility

# Create nltk_data folder inside current working directory
nltk_data_path = os.path.join(os.getcwd(), 'nltk_data')

# Download stopwords if not already present
if not os.path.exists(nltk_data_path):
    os.makedirs(nltk_data_path)
    nltk.download('stopwords', download_dir=nltk_data_path)

# Always ensure nltk uses correct data path
nltk.data.path.append(nltk_data_path)

# Load stopwords
stop_words = set(nltk.corpus.stopwords.words('english'))

# Preprocessing function
def clean_text(text):
    text = text.lower()  # convert to lowercase
    text = re.sub(r'[^a-zA-Z\s]', '', text)  # remove punctuation and numbers
    words = text.split()
    words = [word for word in words if word not in stop_words]
    return ' '.join(words)
