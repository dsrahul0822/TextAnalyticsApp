# pages/3_Data_Visualization.py

import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
from wordcloud import WordCloud
from collections import Counter
import nltk
from nltk.corpus import stopwords
import os

# Download stopwords if not already downloaded
nltk.download('stopwords')
stop_words = set(stopwords.words('english'))

st.title("Step 3️⃣ - Data Visualization")

# Check if data file exists
if not os.path.exists("data/uploaded_data.csv"):
    st.error("No data found. Please upload the data first.")
    st.stop()

# Load data
df = pd.read_csv("data/uploaded_data.csv")

st.write("Sample Data:")
st.dataframe(df.head())

# Combine all reviews into one text
all_text = " ".join(df['Review'].astype(str).tolist())

# Basic text cleaning: lowercasing & removing stopwords
words = all_text.lower().split()
filtered_words = [word for word in words if word not in stop_words and word.isalpha()]

# Word frequency
word_freq = Counter(filtered_words)
top_words = word_freq.most_common(20)

# Bar Chart
st.subheader("Top 20 Word Frequencies")

words, counts = zip(*top_words)
plt.figure(figsize=(10,5))
plt.bar(words, counts)
plt.xticks(rotation=45)
st.pyplot(plt)

# Word Cloud
st.subheader("Word Cloud")

wordcloud = WordCloud(width=800, height=400, background_color='white').generate(" ".join(filtered_words))
plt.figure(figsize=(15,7))
plt.imshow(wordcloud, interpolation='bilinear')
plt.axis('off')
st.pyplot(plt)
