import streamlit as st

# function used to display the output from the model just below the form
def display_agent_response(response):
    sections = response.split("\n\n")
    for section in sections:
        st.markdown(f"**{section.strip()}**")
