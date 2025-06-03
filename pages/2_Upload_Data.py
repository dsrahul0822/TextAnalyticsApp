# pages/2_Upload_Data.py

import streamlit as st
import pandas as pd
import os

# Create data directory if not exists
if not os.path.exists("data"):
    os.makedirs("data")

st.title("Step 2️⃣ - Upload Your Data")

st.markdown("""
**Instructions:**
- File format: `.csv`, `.xlsx`, or `.tsv`
- The file should contain:
    - `Review` column (text data)
    - `Liked` column (target: 1 = positive, 0 = negative)
""")

# Upload file
uploaded_file = st.file_uploader("Upload your dataset", type=["csv", "xlsx", "tsv"])

if uploaded_file is not None:
    try:
        if uploaded_file.name.endswith('.csv'):
            df = pd.read_csv(uploaded_file)
        elif uploaded_file.name.endswith('.xlsx'):
            df = pd.read_excel(uploaded_file)
        elif uploaded_file.name.endswith('.tsv'):
            df = pd.read_csv(uploaded_file, sep='\t')
        else:
            st.error("Unsupported file format.")

        # Check if required columns are present
        if 'Review' in df.columns and 'Liked' in df.columns:
            st.success("✅ File successfully uploaded and verified!")
            st.write("Preview of uploaded data:")
            st.dataframe(df.head())

            # Save file for further processing
            df.to_csv("data/uploaded_data.csv", index=False)
            st.success("File saved for further processing ✅")
        else:
            st.error("Uploaded file must contain 'Review' and 'Liked' columns.")

    except Exception as e:
        st.error(f"Error reading file: {e}")
else:
    st.info("Please upload the dataset.")
