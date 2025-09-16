import gradio as gr
import requests
import os
from dotenv import load_dotenv

# Load API key from .env file
load_dotenv()
GROQ_API_KEY = os.getenv("GROQ_API_KEY")
GROQ_API_URL = "https://api.groq.com/openai/v1/chat/completions"

# Store last three chats as context
chat_history = []

def chat_bot(user_message, history):
    global chat_history
    groq_history = []
    for pair in history[-3:]:
        if pair[0]:
            groq_history.append({"role": "user", "content": pair[0]})
        if pair[1]:
            groq_history.append({"role": "assistant", "content": pair[1]})
    groq_history.append({"role": "user", "content": user_message})
    groq_history = groq_history[-3:]

    payload = {
        "model": "llama-3.3-70b-versatile",  # ✅ updated model
        "messages": groq_history,
        "max_tokens": 150
    }
    headers = {
        "Authorization": f"Bearer {GROQ_API_KEY}",
        "Content-Type": "application/json"
    }
    response = requests.post(GROQ_API_URL, json=payload, headers=headers)
    if response.status_code == 200:
        result = response.json()
        bot_reply = result["choices"][0]["message"]["content"]
        history.append([user_message, bot_reply])
        return "", history
    else:
        error_message = response.json().get("error", {}).get("message", "Unknown error")
        history.append([user_message, f"⚠️ {error_message}"])
        return "", history

with gr.Blocks(title="Groq Chatbot") as demo:
    gr.HTML("""
    <h1 style="text-align:center;
               font-size:32px;
               font-weight:bold;
               background: linear-gradient(90deg, red, orange, yellow, green, blue, indigo, violet);
               background-size: 400% 400%;
               -webkit-background-clip: text;
               -webkit-text-fill-color: transparent;
               animation: rainbow 5s ease infinite;">
        📚 Educational Chatbot
    </h1>
    <style>
    @keyframes rainbow {
        0% { background-position: 0% 50%; }
        50% { background-position: 100% 50%; }
        100% { background-position: 0% 50%; }
    }
    </style>
    """)

    chatbot = gr.Chatbot()
    msg = gr.Textbox(label="Type your message", placeholder="Ask me anything...")
    clear = gr.Button("Clear")

    def clear_fn():
        return [], ""

    msg.submit(chat_bot, [msg, chatbot], [msg, chatbot])
    clear.click(clear_fn, [], [chatbot, msg])

if __name__ == "__main__":
    demo.launch()
