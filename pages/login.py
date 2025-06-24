# login.py
import streamlit as st
from db.database import authenticate_user, register_user

st.set_page_config(page_title="Login - ConsciousDay Agent", layout="centered", initial_sidebar_state="collapsed")

st.title("Login to ConsciousDay Agent")


login_tab, signup_tab = st.tabs(["Login", "Sign Up"])

# ---- LOGIN TAB ----
with login_tab:
    st.subheader("Login")

    username = st.text_input("Username")
    password = st.text_input("Password", type="password")

    if st.button("Login"):
        if authenticate_user(username, password):
            st.success("Login successful!")
            st.session_state["authenticated"] = True
            st.session_state["username"] = username

            # Redirect to main app (Streamlit 1.22+)
            st.switch_page("pages/Homepage.py")
        else:
            st.error("Invalid username or password.")

with signup_tab:
    st.subheader("Create New Account")

    new_username = st.text_input("New Username")
    new_password = st.text_input("New Password", type="password")

    if st.button("Sign Up"):
        if register_user(new_username, new_password):
            st.success("Account created! Please log in.")
        else:
            st.warning("Username already exists.")
