# 🎓 Education Chatbot

An interactive AI-powered chatbot designed to assist students with learning, powered by **Groq API** and a **Gradio interface.

## 🚀 Features
- AI-powered conversational chatbot.
- Context-aware responses (stores recent chat history).
- Simple and user-friendly web UI with **Gradio**.
- Secure API key management with `.env` file.

---

## 🛠️ Tech Stack
- **Python 3.9+**
- **Gradio** (for UI)
- **Groq API** (for AI responses)
- **dotenv** (for environment variable management)
- **Requests** (for API calls)

---

## 📂 Project Structure
Education-Chatbot/
│-- groq_chatbot.py # Main chatbot code
│-- requirements.txt # Python dependencies
│-- .env # Environment file (contains API key)
│-- README.md # Documentation

## ⚙️ Setup & Installation

1. **Clone the repository**
   ```bash
   git clone https://github.com/alatsayali272-del/Education-Chatbot.git
   cd Education-Chatbot

2. Create and activate a virtual environment
python -m venv venv
source venv/bin/activate   # On Mac/Linux
venv\Scripts\activate      # On Windows

3. Install dependencies
pip install -r requirements.txt

4. Add your Groq API key
Create a .env file in the root directory.
Add the following line:
GROQ_API_KEY=your_api_key_here

5. Running the Chatbot
Run the following command:
python groq_chatbot.py


