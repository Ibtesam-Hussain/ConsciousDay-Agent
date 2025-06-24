import streamlit as st
from db.database import init_db


# this app.py will initialize the sqlite3 db and make sure to route the user w.r.t its authentication session

st.set_page_config(page_title="ConsciousDay Agent", layout="centered", initial_sidebar_state="collapsed")

init_db()  # Ensure DB is ready

# Redirect logic to Login page if not authenticated
if "authenticated" not in st.session_state or not st.session_state["authenticated"]:
    st.switch_page("pages/login.py")
else:
    st.switch_page("pages/Homepage.py")
