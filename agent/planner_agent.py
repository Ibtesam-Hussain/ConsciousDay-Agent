import os
from dotenv import load_dotenv
from langchain.prompts import PromptTemplate
from langchain.chat_models import ChatOpenAI  # Chat model
import streamlit as st

# Load environment variables
load_dotenv()

# Template (which is provided in the Hiring test pdf)
prompt_template = """
You are a daily reflection and planning assistant. Your goal is to:
1. Reflect on the user's journal and dream input
2. Interpret the user's emotional and mental state
3. Understand their intention and 3 priorities
4. Generate a practical, energy-aligned strategy for their day

INPUT:
Morning Journal: {journal}
Intention: {intention}
Dream: {dream}
Top 3 Priorities: {priorities}

OUTPUT:
1. Inner Reflection Summary
2. Dream Interpretation Summary
3. Energy/Mindset Insight
4. Suggested Day Strategy (time-aligned tasks)
"""

# Function to run the langchain agent 
def run_agent(journal, intention, dream, priorities):
    # Use ChatOpenAI (works with OpenRouter too)
    # roadmap of ai agents (LangChain framework fro prompting, templates etc -> LLM - OpenRouter Api -> Model - Deepseek r1 (free))
    llm = ChatOpenAI(
        openai_api_base="https://openrouter.ai/api/v1",
        openai_api_key=os.getenv("OPENROUTER_API_KEY") or st.secrets.get("OPENROUTER_API_KEY"),  # <-- this must match your .env
        model_name="deepseek/deepseek-r1-0528:free",
        temperature=0.7,
    )

    # Fill the template with user inputs
    prompt = PromptTemplate.from_template(prompt_template)
    filled_prompt = prompt.format(
        journal=journal, 
        intention=intention, 
        dream=dream, 
        priorities=priorities
    )

    # Call the model
    response = llm.predict(filled_prompt)
    return response
