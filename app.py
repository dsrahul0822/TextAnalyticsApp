# app.py
import streamlit as st
import utils.login as login

# Set Streamlit page configuration
st.set_page_config(page_title="Text Analytics Sentiment App", layout="wide")

# Call login function
if login.login():
    st.sidebar.success("Login Successful!")
    st.sidebar.markdown("Select a page from the sidebar")
else:
    st.stop()
