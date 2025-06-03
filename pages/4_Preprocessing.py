# pages/4_Preprocessing.py

import streamlit as st
import pandas as pd
import os
import joblib
from sklearn.feature_extraction.text import CountVectorizer
from utils.preprocessing import clean_text

# Create vectorizer folder if not exists
if not os.path.exists("vectorizer"):
    os.makedirs("vectorizer")

st.title("Step 4️⃣ - Data Preprocessing")

# Check if data file exists
if not os.path.exists("data/uploaded_data.csv"):
    st.error("No data found. Please upload the data first.")
    st.stop()

# Load data
df = pd.read_csv("data/uploaded_data.csv")
st.write("Sample Data Before Cleaning:")
st.dataframe(df.head())

# Apply cleaning
df['Clean_Review'] = df['Review'].apply(clean_text)
st.write("Sample Data After Cleaning:")
st.dataframe(df[['Review', 'Clean_Review', 'Liked']].head())

# Apply CountVectorizer
st.subheader("Feature Extraction - CountVectorizer")

# Fit vectorizer on clean data
vectorizer = CountVectorizer()
X = vectorizer.fit_transform(df['Clean_Review'])

st.write(f"Total Features Extracted: {len(vectorizer.get_feature_names_out())}")

# Save vectorizer for future use
joblib.dump(vectorizer, "vectorizer/vectorizer.pkl")
st.success("Vectorizer saved successfully ✅")

# Save preprocessed data
df.to_csv("data/preprocessed_data.csv", index=False)
st.success("Preprocessed data saved successfully ✅")
