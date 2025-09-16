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

## Explanation of the code :

gradio → Builds the chatbot web UI.
requests → Sends HTTP requests to the Groq API.
os → Reads environment variables.
dotenv → Loads the .env file so we can securely use the API key.

2.Loading the API Key :

Loads your Groq API key from .env.
If the key is missing, it raises an error instead of crashing later.

3. Chat History Management

chat_history = []
Stores the last three user–assistant exchanges so the bot can answer with short-term memory.

4. Chatbot Function :

Converts the last 3 chat turns into a format Groq API understands (role: user/assistant).
Adds the new user message at the end.

5. Sending Request to Groq API

Prepares a JSON payload with:
Model → "llama-3.3-70b-versatile"
Conversation history (messages)
Response length (max_tokens)
Sends it to Groq’s chat completions endpoint.

6. Handling the Response

If successful → Extracts chatbot reply and updates history.
If error → Displays the error message inside the chat window.

7. Building the Gradio UI

Uses Gradio Blocks to build a UI.
Adds a rainbow-colored animated title.

8. Adding Components

chatbot = gr.Chatbot()
msg = gr.Textbox(label="Type your message", placeholder="Ask me anything...")
clear = gr.Button("Clear")

gr.Chatbot() → Displays conversation history.
gr.Textbox() → Lets the user type messages.
gr.Button("Clear") → Clears chat history.

9. Clear Function

def clear_fn():
    return [], 

Resets the chat history and clears the input box.

10. Event Bindings

msg.submit(chat_bot, [msg, chatbot], [msg, chatbot])
clear.click(clear_fn, [], [chatbot, msg])

Submitting the textbox runs chat_bot().
Clicking Clear runs clear_fn().

11. Launching the App 

if __name__ == "__main__":
    demo.launch()

Starts the Gradio app → Opens a local browser window with your chatbot UI.



