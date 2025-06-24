# 🌞 ConsciousDay Agent

An intelligent **daily reflection and planning assistant** built with `Streamlit`, `LangChain`, and `OpenRouter`. This AI-powered web app helps users reflect on their mindset, dreams, and intentions, then generates a focused day plan.

---

## 🚀 Features

- ✍️ **Morning Journal**: Input journal, dreams, intentions & top priorities.
- 🤖 **AI Response**: Returns:
  - Inner Reflection
  - Dream Interpretation
  - Mindset Insight
  - Day Strategy
- 🧠 **LLM via OpenRouter** (`deepseek/deepseek-r1-0528:free`)
- 👤 **User Authentication** with login/signup via `SQLite3`
- 🗂️ **Multi-Entry History Viewer** by date
- 🔐 **Session Persistence** to retain login state
- 🎨 **Custom UI**: Collapsed sidebar, top header, buttons

## 🧠 Tech Stack

- `Streamlit` (Web UI)
- `LangChain` (Prompt and LLM integration)
- `OpenRouter` (LLM gateway)
- `SQLite3` (User & journal database)
- `Python-dotenv` (Environment secrets)

---

## 🔧 Setup Instructions

1. **Clone the repo**:
```bash
    git clone https://github.com/your-username/ConsciousDay-Agent.git
    cd ConsciousDay-Agent
```bash

## 🧪 Sample Input

**Journal:**

> Feeling grateful, but a bit stressed about deadlines.

**Dream:**

> I was climbing stairs endlessly in a dark building.

**Intention:**

> Stay calm and focused.

**Priorities:**

- Submit report  
- Team call  
- Evening workout  

---

## ✅ Features Completed

- 🔐 Login & Sign-up with **user-specific** data
- 🧠 Daily agent response powered by **LangChain** + **OpenRouter**
- 🗓️ Multi-entry journal support for the same day
- 🎨 Improved layout with custom UI enhancements
- 🔑 Secure environment variable handling (`.env` / `secrets.toml`)
- 🧾 Session-controlled access & logout system

---

## 🧠 Model Details

- **Model**: `deepseek/deepseek-r1-0528:free`  
- **Provider**: [OpenRouter.ai](https://openrouter.ai)  
- **Frameworks Used**: `LangChain`, `Streamlit`

---

## ✨ Future Enhancements

- 📤 Export history as **PDF**
- 🔄 **Model switcher** (free/paid toggle)
- 📊 Mood tracking with daily/weekly **graphs**
- 🛠️ **Admin dashboard** for managing user entries and logs

---

## 🤝 Built With

- [Streamlit](https://streamlit.io/)
- [LangChain](https://www.langchain.com/)
- [OpenRouter](https://openrouter.ai)
- [DeepSeek](https://deepseek.com)

---

> Made with ❤️ for mental clarity and intentional living.




