# pages/6_Prediction.py

import streamlit as st
import joblib
import os
from utils.preprocessing import clean_text

st.title("Step 6️⃣ - Live Prediction")

# Allow user to select trained model
model_type = st.selectbox("Select Trained Model", ["Logistic Regression", "Naive Bayes"])

model_filename = f"models/{model_type.replace(' ','_')}_model.pkl"
vectorizer_filename = f"vectorizer/{model_type.replace(' ','_')}_vectorizer.pkl"

# Check if model files exist
if not os.path.exists(model_filename) or not os.path.exists(vectorizer_filename):
    st.error(f"Trained model or vectorizer not found for {model_type}. Please train the model first.")
    st.stop()

# Load model and vectorizer
model = joblib.load(model_filename)
vectorizer = joblib.load(vectorizer_filename)

# Take user input
user_input = st.text_area("Enter Feedback for Prediction:")

if st.button("Predict"):
    if user_input.strip() == "":
        st.warning("Please enter some text for prediction.")
    else:
        # Preprocess input
        cleaned_input = clean_text(user_input)
        vectorized_input = vectorizer.transform([cleaned_input])
        
        # Predict
        prediction = model.predict(vectorized_input)[0]
        probability = model.predict_proba(vectorized_input)[0]
        
        sentiment = "Positive" if prediction == 1 else "Negative"
        prob = probability[1] if prediction == 1 else probability[0]
        
        st.subheader(f"Predicted Sentiment: {sentiment}")
        st.write(f"Confidence: {prob*100:.2f}%")
