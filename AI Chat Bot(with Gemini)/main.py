# chatbot/app_day1_prompt.py

# Import all required modules
import time
import os
import joblib
import google.generativeai as genai
from dotenv import load_dotenv

# Step 1: Introduction
print("💬 Welcome to the ASTROBOT Chatbot Project!")
print("We'll build a chatbot step by step using Google Gemini API.")
print("Follow the prompts to set up your chatbot. 🚀\n")

# Step 2: Configure the API Key
print("Step 1: Configure your API Key")
print("Hint: Add your API Key to a `.env` file or enter it now.")
GOOGLE_API_KEY = os.getenv('GOOGLE_API_KEY')

print("\nSetting up Gemini API...")
load_dotenv()

# Load the API key from `.env` if not provided
if not GOOGLE_API_KEY:
    GOOGLE_API_KEY = os.getenv('GOOGLE_API_KEY')

# Exit if no API key is found
if not GOOGLE_API_KEY:
    print("❌ Error: API Key not found. Please set it in `.env` or input it manually.")
    exit(1)

# Configure the Gemini API
genai.configure(api_key=GOOGLE_API_KEY)
print("✅ Gemini API configured successfully!\n")

# Step 3: Create a Unique Chat Session
print("Step 2: Create a unique chat session.")
chat_title = input("Enter a name for your chat session (default: 'ChatSession'): ") or "ChatSession"
new_chat_id = f"{time.time()}"

# Step 4: Ensure the data folder exists
if not os.path.exists('data/'):
    os.mkdir('data/')

# Load previous chat sessions if available
try:
    past_chats = joblib.load('data/past_chats_list')
    print("\nPrevious chat sessions loaded successfully.")
except FileNotFoundError:
    past_chats = {}
    print("\nNo previous chat sessions found. Starting fresh.")

# Initialize the Gemini model
print("\nInitializing the generative model...")
model = genai.GenerativeModel('gemini-pro')
chat = model.start_chat()
print("✅ Model initialized successfully!")

# Step 5: Load chat history
try:
    messages = joblib.load(f"data/{new_chat_id}-messages")
except FileNotFoundError:
    messages = []  # Initialize an empty list if no history exists

# Step 6: Start the Chat Session
print("\n🎉 Your chatbot is ready! Let's start chatting.")
print("Type 'exit' to end the chat.\n")

# Save the new chat session if it doesn't already exist
if new_chat_id not in past_chats:
    past_chats[new_chat_id] = chat_title
    joblib.dump(past_chats, 'data/past_chats_list')

# Chat loop
while True:
    user_input = input(f"{chat_title} (You): ")
    if user_input.lower() == 'exit':
        print("🛑 Chat session ended.")
        break

    # Send the user's input to the model and receive a response
    response = chat.send_message(user_input)
    print(f"ASTROBOT: {response.text}")

    # Append user and AI messages to the chat history
    messages.append({'role': 'user', 'content': user_input})
    messages.append({'role': 'ai', 'content': response.text})

    # Save the updated chat history
    joblib.dump(messages, f"data/{new_chat_id}-messages")
    print("💾 Chat history saved.\n")