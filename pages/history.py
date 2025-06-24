import streamlit as st
import sqlite3
from db.database import get_entries_by_date
from datetime import datetime

# Require login
if "authenticated" not in st.session_state or not st.session_state["authenticated"]:
    st.warning("Please login first.")
    st.stop()

username = st.session_state["username"]

st.title("📜 View Previous Reflections")
selected_date = st.date_input("📅 Choose a date to view entries:")
selected_date_str = selected_date.strftime("%Y-%m-%d")

try:
    # Attempt to fetch entries
    entries = get_entries_by_date(selected_date_str, username)

    if entries:
        st.success(f"✅ Found {len(entries)} entries for {selected_date_str}:")

        for i, entry in enumerate(entries, start=1):
            st.markdown("---")
            st.markdown(f"### 📝 Entry #{i}")
            
            st.subheader("📝 Journal")
            st.write(entry[2])

            st.subheader("💤 Dream")
            st.write(entry[4])

            st.subheader("🧠 Reflection & Strategy")
            st.write(entry[6])  # You can split if needed
    else:
        st.info("No entries found for this date yet.")

except sqlite3.OperationalError as e:
    # Catch DB schema issues
    st.error("⚠️ Could not load entries. The database may be missing the required columns.")
    st.exception(e)
    st.info("Try reinitializing your database or contacting the developer.")
