# pages/1_Introduction.py
import streamlit as st

st.title("Text Analytics - Sentiment Classification App")

st.markdown("""
Welcome to the Text Analytics Application!

**Main Features:**

- Upload your dataset (.csv / .xlsx)
- Visualize data with bar chart & word cloud
- Text preprocessing (cleaning, stopwords, punctuation removal)
- Feature extraction using CountVectorizer
- Train models: Logistic Regression / Naive Bayes
- Make live predictions on new text

This application will help you classify customer feedback as Positive or Negative.

👉 Use the sidebar to navigate through the different steps.
""")
