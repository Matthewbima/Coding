import os
import joblib
import google.generativeai as genai
import streamlit as st
import time
from dotenv import load_dotenv

# Step 1: Introduction
print("💬 Welcome to the ASTROBOT Chatbot Project!")
print("We'll build a chatbot step by step using Google Gemini API.")
print("Follow the prompts to set up your chatbot. 🚀\n")

# Load environment variables
load_dotenv()

# Step 2: Configure the API Key
print("Step 1: Configure your API Key")
GOOGLE_API_KEY = os.getenv('GOOGLE_API_KEY')

if not GOOGLE_API_KEY:
    print("❌ Error: API Key not found. Please set it in `.env` file.")
    exit(1)

# Configure the Gemini API
try:
    genai.configure(api_key=GOOGLE_API_KEY)
    print("✅ Gemini API configured successfully!\n")
except Exception as e:
    print(f"❌ Error configuring Gemini API: {e}")
    exit(1)

# Unleash Your Chatbot with Streamlit
new_chat_id = str(int(time.time()))
os.makedirs('data/', exist_ok=True)

# Load old chats
try:
    past_chats = joblib.load('data/past_chats_list')
except FileNotFoundError:
    past_chats = {}
except Exception as e:
    print(f"❌ Error loading past chats: {e}")
    past_chats = {}

# Build the Streamlit sidebar
with st.sidebar:
    st.title('Past Chats')
    if 'chat_id' not in st.session_state:
        st.session_state.chat_id = new_chat_id
    st.session_state.chat_id = st.selectbox(
        label='Pick a past chat',
        options=[new_chat_id] + list(past_chats.keys()),
        format_func=lambda x: past_chats.get(x, 'New Chat'),
    )
    st.session_state.chat_title = f'ChatSession-{st.session_state.chat_id}'

# App title
st.title('Chat with ASTROBOT')
new_chat_id = f'{time.time()}'
MODEL_ROLE = 'ai'
AI_AVATAR_ICON = '🤖'
# Load old chat history
try:
    st.session_state.messages = joblib.load(f'data/{st.session_state.chat_id}-st_messages')
    st.session_state.gemini_history = joblib.load(f'data/{st.session_state.chat_id}-gemini_messages')
except FileNotFoundError:
    st.session_state.messages = []
    st.session_state.gemini_history = []
except Exception as e:
    st.error(f"Error loading chat history: {e}")



# dev model AI generative Gemini
st.session_state.model = genai.GenerativeModel('gemini-pro')
st.session_state.chat = st.session_state.model.start_chat(history=st.session_state.gemini_history)

# show all chat in history chat in chat history
for message in st.session_state.messages:
    with st.chat_message(name=message['role'], avatar=message.get('avatar')):
        st.markdown(message['content'])

# Handle user input
if prompt := st.chat_input('Your message here...'):
    if st.session_state.chat_id not in past_chats.keys():
        past_chats[st.session_state.chat_id] = st.session_state.chat_title
        joblib.dump(past_chats, 'data/past_chats_list')

    with st.chat_message('user'):
        st.markdown(prompt)
    st.session_state.messages.append(dict(role='user', content=prompt))

#Generate AI Response
    response = st.session_state.chat.send_message(prompt, stream=True)
    with st.chat_message(name=MODEL_ROLE, avatar=AI_AVATAR_ICON):
        message_placeholder = st.empty()
        full_response = ''

        for chunk in response:
            for ch in chunk.text.split(' '):
                full_response += ch + ' '
                time.sleep(0.05)
                message_placeholder.write(full_response + '▌')
        message_placeholder.write(full_response)


#Save Chat Data
    st.session_state.messages.append(dict(role=MODEL_ROLE, content=full_response, avatar=AI_AVATAR_ICON))
    st.session_state.gemini_history = st.session_state.chat.history

    joblib.dump(st.session_state.messages, f'data/{st.session_state.chat_id}-st_messages')
    joblib.dump(st.session_state.gemini_history, f'data/{st.session_state.chat_id}-gemini_messages')