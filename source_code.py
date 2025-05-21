import streamlit as st
import google.generativeai as genai
from datetime import datetime
import re
from typing import Optional

st.set_page_config(
    page_title="Questa",
    page_icon="🤖",
    layout="centered",
    initial_sidebar_state="collapsed"
)

# Custom CSS for better styling
st.markdown("""
    <style>
        /* Main container */
        .main {
            padding: 0rem 1rem;
        }
        
        /* Chat container */
        .stChatFloatingInputContainer {
            border-top: 1px solid #e0e0e0;
            padding-top: 1rem;
            background-color: #f9f9f9;
        }
        
        /* Message bubbles */
        .stChatMessage {
            background-color: white;
            border-radius: 15px;
            padding: 1rem;
            margin: 0.5rem 0;
            box-shadow: 0 2px 4px rgba(0,0,0,0.1);
        }
        
        /* User name form */
        .stForm {
            background-color: white;
            padding: 2rem;
            border-radius: 10px;
            box-shadow: 0 2px 4px rgba(0,0,0,0.1);
        }
        
        /* Title styling */
        .title-container {
            text-align: center;
            padding: 2rem 0;
            background: linear-gradient(90deg, #4CAF50, #2196F3);
            border-radius: 0 0 20px 20px;
            margin-bottom: 2rem;
        }
        
        .title-text {
            color: white;
            font-size: 2.5rem;
            font-weight: bold;
            margin: 0;
            padding: 0;
        }
        
        .subtitle-text {
            color: rgba(255,255,255,0.9);
            font-size: 1rem;
            margin-top: 0.5rem;
        }
        
        /* Custom button styling */
        .stButton>button {
            background-color: #2196F3;
            color: white;
            border-radius: 20px;
            padding: 0.5rem 2rem;
            border: none;
            box-shadow: 0 2px 4px rgba(0,0,0,0.1);
            transition: all 0.3s ease;
        }
        
        .stButton>button:hover {
            background-color: #1976D2;
            box-shadow: 0 4px 8px rgba(0,0,0,0.2);
        }
        
        /* Input field styling */
        .stTextInput>div>div>input {
            border-radius: 20px;
            border: 2px solid #e0e0e0;
            padding: 0.5rem 1rem;
        }
        
        /* Chat input styling */
        .stChatInputContainer {
            border-top: 1px solid #e0e0e0;
            padding-top: 1rem;
        }
    </style>
""", unsafe_allow_html=True)


class Chatbot:
    def __init__(self, api_key: str):
        genai.configure(api_key=api_key)
        self.model = genai.GenerativeModel('gemini-pro')
        self.chat = self.model.start_chat(history=[])
        
        self.intents = {
            'weather': r'\b(weather|temperature|rainfall|forecast)\b',
            'time': r'\b(time|hour|clock)\b',
            'greeting': r'\b(hello|hi|hey|greetings)\b'
        }
        
        # Add emoji mappings
        self.emoji_patterns = {
            r'\b(happy|joy|glad|delighted)\b': '😊',
            r'\b(sad|upset|unhappy)\b': '😔',
            r'\b(laugh|lol|haha)\b': '😄',
            r'\b(love|heart|adore)\b': '❤️',
            r'\b(weather|sun|sunny)\b': '☀️',
            r'\b(rain|rainy|raining)\b': '🌧️',
            r'\b(cloud|cloudy)\b': '☁️',
            r'\b(snow|snowing|snowy)\b': '❄️',
            r'\b(think|thinking|thought)\b': '🤔',
            r'\b(book|read|reading)\b': '📚',
            r'\b(music|song|singing)\b': '🎵',
            r'\b(food|eat|eating)\b': '🍽️',
            r'\b(work|working|job)\b': '💼',
            r'\b(sleep|sleeping|tired)\b': '😴',
            r'\b(phone|call|calling)\b': '📱',
            r'\b(mail|email|message)\b': '📧',
            r'\b(money|dollar|payment)\b': '💰',
            r'\b(time|clock|hour)\b': '⏰',
            r'\b(star|stars)\b': '⭐',
            r'\b(fire|hot|flame)\b': '🔥'
        }

    def add_emojis(self, text: str) -> str:
        """Add relevant emojis to the text based on keyword matching."""
        modified_text = text
        for pattern, emoji in self.emoji_patterns.items():
            # Find all matches of the pattern in the text (case-insensitive)
            matches = re.finditer(pattern, modified_text, re.IGNORECASE)
            
            # Add emoji after each matched word, avoiding duplicates
            offset = 0
            for match in matches:
                # Only add emoji if it's not already present right after the word
                end_pos = match.end() + offset
                if end_pos >= len(modified_text) or modified_text[end_pos:end_pos+2] != emoji:
                    modified_text = modified_text[:end_pos] + ' ' + emoji + ' ' + modified_text[end_pos:]
                    offset += len(emoji) + 2  # Account for added emoji and spaces
                    
        return modified_text

    def detect_intent(self, message: str) -> Optional[str]:
        message = message.lower()
        for intent, pattern in self.intents.items():
            if re.search(pattern, message):
                return intent
        return None

    def handle_special_intents(self, intent: str) -> Optional[str]:
        if intent == 'time':
            current_time = datetime.now().strftime("%I:%M %p")
            return f"The current time is {current_time} ⏰"
        elif intent == 'weather':
            return "I don't have access to real-time weather data ☁️, but I can chat about the weather in general!"
        elif intent == 'greeting':
            if st.session_state.user_name:
                return f"Hello {st.session_state.user_name}! 👋 How can I assist you today?"
            return "Hello! 👋 How can I assist you today?"
        return None

    def generate_response(self, user_input: str) -> str:
        if not user_input.strip():
            return "I noticed you sent an empty message. How can I help you? 🤔"

        intent = self.detect_intent(user_input)
        if intent:
            special_response = self.handle_special_intents(intent)
            if special_response:
                return special_response

        try:
            response = self.chat.send_message(user_input)
            # Add emojis to the response
            enhanced_response = self.add_emojis(response.text)
            return enhanced_response
        except Exception as e:
            return "I'm sorry, I'm having trouble understanding. Could you please rephrase that? 😅"


def main():
    # Custom title with gradient background
    st.markdown("""
        <div class="title-container">
            <h1 class="title-text">Questa</h1>
            <p class="subtitle-text">Your intelligent companion</p>
        </div>
    """, unsafe_allow_html=True)
    
    # Get API key
    st.session_state.GOOGLE_API_KEY = 'Enter your API KEY' # use google suite for api generation

    # Initialize session state
    if 'chat_history' not in st.session_state:
        st.session_state.chat_history = []
    if 'user_name' not in st.session_state:
        st.session_state.user_name = None
    if 'chatbot' not in st.session_state:
        st.session_state.chatbot = Chatbot(st.session_state.GOOGLE_API_KEY)

    # User name input with improved styling
    if st.session_state.user_name is None:
        st.markdown("""
            <div style='text-align: center; margin-bottom: 2rem;'>
                <h2>Welcome! 👋</h2>
                <p>Please introduce yourself to get started.</p>
            </div>
        """, unsafe_allow_html=True)
        
        with st.form("name_form"):
            user_name = st.text_input("", placeholder="Enter your name...")
            submit_button = st.form_submit_button("Start Chatting")
            if submit_button and user_name.strip():
                st.session_state.user_name = user_name
                st.session_state.chat_history.append(("bot", f"Hi {user_name}! How can I help you today?"))
                st.rerun()

    # Chat interface
    if st.session_state.user_name:
        # Display chat history with improved styling
        for role, message in st.session_state.chat_history:
            with st.chat_message(role, avatar="🤖" if role == "bot" else None):
                st.write(message)

        # Chat input
        if prompt := st.chat_input(placeholder="Type your message here..."):
            with st.chat_message("user"):
                st.write(prompt)
            st.session_state.chat_history.append(("user", prompt))

            with st.chat_message("bot", avatar="🤖"):
                response = st.session_state.chatbot.generate_response(prompt)
                st.write(response)
            st.session_state.chat_history.append(("bot", response))

if __name__ == "__main__":
    main()
