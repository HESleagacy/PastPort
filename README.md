#  Historical Events Finder (LangChain + Gemini)

A mini Streamlit app that uses **LangChain** and **Google Gemini (via `langchain-google-genai`)**  
to fetch and display **important global events** that happened on a given date.

---

##  Features
- Enter any date **before 2025** and get a list of significant global events.
- If the date exceeds 2024 → app politely asks for a valid date.
- If no major events are found → app finds the **closest date with events**.
- Powered by **Gemini 1.5 Flash** through LangChain’s `ChatGoogleGenerativeAI`.
- Simple, clean **Streamlit interface**.

---

##  Tech Stack
- **Python 3.10+**
- **Streamlit** – frontend for quick prototyping
- **LangChain** – prompt templates + LLM integration
- **Google Gemini API** – LLM backend
- **python-dotenv** – manage API keys securely

---
<img width="1366" height="697" alt="Screenshot from 2025-09-15 20-12-19" src="https://github.com/user-attachments/assets/c40b58f3-36f3-4161-9682-404fa23d28d8" />
