# utils/login.py
import streamlit as st

def login():
    st.sidebar.header("Login")

    username = st.sidebar.text_input("Username")
    password = st.sidebar.text_input("Password", type="password")

    if st.sidebar.button("Login"):
        if username == "admin" and password == "admin123":
            return True
        else:
            st.sidebar.error("Invalid Credentials")
            return False
    else:
        return False
