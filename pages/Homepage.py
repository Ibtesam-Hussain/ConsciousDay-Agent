import streamlit as st
from components.input_form import user_input_form
from components.output_display import display_agent_response
from agent.planner_agent import run_agent
from db.database import init_db, save_entry
from datetime import date
import os
from dotenv import load_dotenv



# Hide the sidebar toggle arrow (>>)
hide_sidebar_style = """
    <style>
        [data-testid="collapsedControl"] {
            display: none;
        }
    </style>
"""
st.markdown(hide_sidebar_style, unsafe_allow_html=True)

# Require authentication
if "authenticated" not in st.session_state or not st.session_state["authenticated"]:
    st.warning("Please login from the Login page.")
    st.stop()

username = st.session_state["username"]

# Page config
st.set_page_config(page_title="ConsciousDay Agent", layout="centered", initial_sidebar_state="collapsed")
init_db()
load_dotenv()

st.title("ConsciousDay Agent")

#  Header Row with Welcome + Buttons
col1, col2, col3 = st.columns([2, 1, 2])

with col1:
    st.markdown(f"#### Welcome, **{username}**")

with col3:
    col_btn1, col_btn2 = st.columns([1, 1])
    with col_btn1:
        if st.button("View History"):
            st.switch_page("pages/history.py")
    with col_btn2:
        if st.button("🔓 Logout"):
            st.session_state.clear()
            st.success("Logged out successfully!")
            st.switch_page("pages/login.py")

# Journal form
submitted, journal, dream, intention, priorities = user_input_form()

if submitted:
    # Validate all fields before continuing
    if not journal or not dream or not intention or not priorities:
        st.error("⚠️ Please fill in all fields before submitting.")
    else:
        with st.spinner("Generating your reflection and day strategy..."):
            response = run_agent(journal, intention, dream, priorities)
            display_agent_response(response)

            save_entry(
                date.today().isoformat(),
                journal,
                intention,
                dream,
                priorities,
                response,
                response,
                username
            )

            st.success("✅ Saved Successfully!")

# Footer (model info)
st.markdown(
    "<h6 style='text-align: center;'>LLM Model used: Deepseek-r1-0528 (free)</h6>",
    unsafe_allow_html=True
)
