# 🤖 BP’s Agent

An AI-powered chatbot built with **Streamlit**, **Langchain**, and **Groq's LLaMA-3.3 70B model** that offers answers with politeness and style. Designed to be helpful, interactive, and developer-friendly — it's your tech bro guru in a box.

---

## 🛠 Features

- ✨ LLaMA 3.3 70B via Groq API
- 🎨 Stylish Streamlit UI with custom CSS
- 🧠 Polite, accurate responses with a custom system prompt
- 📦 Easy-to-run local app

---

## 🚀 Setup Instructions

 1. Clone the repository

bash
git clone https://github.com/BpReddy1104/Bp-s_AI_Agent
Bp-s_AI_Agent

2. Install dependencies
Make sure you have Python 3.8 or later.
pip install -r requirements.txt

3. Create .env file
Create a .env file in the project root and add your Groq API key:
GROQ_API_KEY=your_groq_api_key_here

4. Run the app
streamlit run app.py

📁 Project Structure
bps-dev-chatbot/
│
├── app.py             # Streamlit app logic
├── .env               # API keys (not committed)
├── requirements.txt   # Dependencies
└── README.md          # Project documentation

📸 UI Preview
![image](https://github.com/user-attachments/assets/a0741b33-4e88-4270-8b76-30e566982459)

![image](https://github.com/user-attachments/assets/a07f81c2-6b4c-4e12-b1fa-417bd908bff4)



🔐 Environment Variables
Variable	Description
GROQ_API_KEY	Your Groq API Key

🧠 Tech Stack
Frontend: Streamlit

LLM: Langchain + Groq API (llama-3.3-70b-versatile)

Backend Logic: Python
🤝 Credits
Built with 💻 by BP — your friendly tech bro.
