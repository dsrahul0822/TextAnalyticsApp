# pages/7_File_Explorer.py

import streamlit as st
import os

st.title("Internal File Explorer (Streamlit Cloud Runtime)")

folders_to_check = ['data', 'models', 'vectorizer']

for folder in folders_to_check:
    st.header(f"📂 Folder: {folder}")
    
    if not os.path.exists(folder):
        st.warning(f"{folder} folder does not exist.")
        continue

    files = os.listdir(folder)
    
    if not files:
        st.info("No files found in this folder.")
    else:
        for file in files:
            filepath = os.path.join(folder, file)
            file_size = os.path.getsize(filepath) / 1024  # size in KB
            st.write(f"📄 {file} — {file_size:.2f} KB")
