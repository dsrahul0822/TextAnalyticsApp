# pages/5_Model_Training.py

import streamlit as st
import pandas as pd
import joblib
import numpy as np
import os
from utils.model import train_model
from sklearn.feature_extraction.text import CountVectorizer

st.title("Step 5️⃣ - Model Training")

# Check files exist
if not os.path.exists("data/preprocessed_data.csv") or not os.path.exists("vectorizer/vectorizer.pkl"):
    st.error("Preprocessed data or vectorizer not found. Please complete previous steps.")
    st.stop()

# Load data & vectorizer
df = pd.read_csv("data/preprocessed_data.csv")
vectorizer = joblib.load("vectorizer/vectorizer.pkl")

st.write("Sample Data:")
st.dataframe(df[['Clean_Review', 'Liked']].head())

# Total features
total_features = len(vectorizer.get_feature_names_out())
st.write(f"Total features available: {total_features}")

# Select number of features
num_features = st.slider("Select number of features to use", 100, total_features, 1500 if total_features >= 1500 else total_features)

# Reduce features using top frequent words
sorted_vocab = vectorizer.vocabulary_
sorted_vocab = dict(sorted(sorted_vocab.items(), key=lambda item: item[1])[:num_features])

# Create new vectorizer with limited features
limited_vectorizer = CountVectorizer(vocabulary=sorted_vocab)
X = limited_vectorizer.fit_transform(df['Clean_Review'])
y = df['Liked']

# Model selection
model_type = st.selectbox("Select Model", ["Logistic Regression", "Naive Bayes"])

if st.button("Train Model"):
    model, acc = train_model(X, y, model_type)
    
    # Ensure models directory exists
    if not os.path.exists("models"):
        os.makedirs("models")
    
    # Ensure vectorizer directory exists
    if not os.path.exists("vectorizer"):
        os.makedirs("vectorizer")
    
    # Save model and vectorizer
    model_filename = f"models/{model_type.replace(' ','_')}_model.pkl"
    vectorizer_filename = f"vectorizer/{model_type.replace(' ','_')}_vectorizer.pkl"
    
    joblib.dump(model, model_filename)
    joblib.dump(limited_vectorizer, vectorizer_filename)

    st.success(f"{model_type} trained successfully with accuracy: {acc:.2%}")
