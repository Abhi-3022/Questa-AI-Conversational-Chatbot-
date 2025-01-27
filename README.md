# Questa - Your Intelligent Chat Companion 🤖

Questa is an advanced chatbot application designed to deliver an engaging, intelligent, and emoji-enriched conversational experience. Leveraging Google's Generative AI with Gemini models, Questa provides personalized responses while handling special intents like greetings, weather discussions, and time queries.

---

## General Overview 📖

### Key Features:
- **Generative AI Integration**: Powered by Google's Generative AI model "Gemini-Pro."
- **Customizable Responses**: Includes emojis to make conversations more lively and relatable.
- **Intent Recognition**: Detects user intents such as greetings, weather-related queries, and time inquiries.
- **Streamlit Interface**: User-friendly web application for seamless interactions.
- **Enhanced Styling**: Modern and intuitive UI with custom CSS styling for better usability.

### How It Works:
1. Users interact with Questa via the Streamlit web interface.
2. Messages are processed for intent recognition and context.
3. Responses are enhanced with relevant emojis and displayed in a chat-like format.
4. Special intents like "time" and "greetings" are handled uniquely for added personalization.

---

## How to Use / Run Questa 🚀

### Prerequisites:
1. Python 3.8+
2. Google Generative AI API Key (replace `st.session_state.GOOGLE_API_KEY` in the code with your API key).
3. Install dependencies:
   ```bash
   pip install streamlit google-generativeai
   ```

### Steps to Run:
1. Clone this repository:
   ```bash
   git clone https://github.com/<your-username>/questa.git
   cd questa
   ```
2. Start the application:
   ```bash
   streamlit run questa.py
   ```
3. Open the application in your browser at `http://localhost:8501`.

4. Enter your name to get started and start chatting with Questa!

---

## Sample Input and Output 🎯

### Sample Input:
**User:** "Hi there! Can you tell me the time?"

### Sample Output:
**Bot:** "Hello! 👋 How can I assist you today?"
**Bot:** "The current time is 02:45 PM ⏰"

### Sample Input:
**User:** "It's sunny today."

### Sample Output:
**Bot:** "That's great to hear! ☀️ What's on your mind?"

---

## Project Description 🛠️
Questa uses the Gemini-Pro model by Google Generative AI to generate intelligent, context-aware responses. By integrating custom regex-based intent detection and emoji enrichment, Questa ensures that conversations feel natural and engaging. The modern Streamlit UI provides a seamless user experience with responsive design and intuitive chat functionalities.

---

## File Structure 📂
- **`questa.py`**: Main application file containing the chatbot logic and Streamlit UI implementation.
- **`requirements.txt`**: Lists all Python dependencies.

---

## Future Enhancements ✨
1. Real-time weather data integration.
2. Support for additional languages.
3. Persistent chat history storage.
4. Voice interaction capabilities.

---

## Contributing 🙌
We welcome contributions to Questa! Please feel free to submit a pull request or create an issue for feature requests or bug reports.

---

## Acknowledgments 💡
Special thanks to Google Generative AI and Streamlit for making this project possible.

## Visit here - [https://questa.streamlit.app/]
