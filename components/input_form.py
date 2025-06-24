import streamlit as st



# function used for taking user input about their conscious from the frontend
def user_input_form():
    with st.form("reflection_form"):
        journal = st.text_area("📝 Morning Journal", height=100)
        dream = st.text_area("💤 Dream", height=80)
        intention = st.text_input("🎯 Intention of the Day")
        priorities = st.text_input("✅ Top 3 Priorities (comma-separated)")

        submitted = st.form_submit_button("Submit")

        if submitted:
            if not journal.strip() or not dream.strip() or not intention.strip() or not priorities.strip():
                st.error("⚠️ All fields are required. Please fill out the complete form.")
                return False, journal, dream, intention, priorities

        return submitted, journal, dream, intention, priorities

