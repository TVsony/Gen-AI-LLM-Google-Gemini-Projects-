# Import necessary libraries
from dotenv import load_dotenv  # For loading environment variables from .env file
import streamlit as st  # Streamlit for creating the web interface
import os  # For managing environment variables
import google.generativeai as genai  # Google Gemini API for handling chat and Q&A

# Load environment variables from the .env file, which includes the Google API key
load_dotenv()

# Configure the Google Gemini API with the API key
genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

# Initialize the Gemini model for general language tasks
model = genai.GenerativeModel("gemini-pro")
chat = model.start_chat(history=[])  # Start a chat session with an empty history

# Function to get responses from the Gemini chat model
def get_gemini_response(question):
    # Send the user’s question to the Gemini model with streaming enabled for real-time responses
    response = chat.send_message(question, stream=True)
    return response

# Set up Streamlit for the web application
st.set_page_config(page_title="Q&A Demo")  # Set page title
st.header("Gemini LLM Q/A and chatbot Application")  # Display app header

# Initialize the session state to store chat history, if not already set
if 'chat_history' not in st.session_state:
    st.session_state['chat_history'] = []

# Text input box for user questions
input = st.text_input("Input: ", key="input")

# Button to submit the question
submit = st.button("Ask the question")

# When the user submits a question
if submit and input:
    response = get_gemini_response(input)  # Get the Gemini model's response to the question
    
    # Append the user question to the session state chat history
    st.session_state['chat_history'].append(("You", input))
    
    # Display the response header
    st.subheader("The Response is")
    
    # Iterate over streamed response chunks and display each text chunk
    for chunk in response:
        st.write(chunk.text)
        # Append each chunk of the model’s response to the session state chat history
        st.session_state['chat_history'].append(("Bot", chunk.text))

# Display all past chat messages
st.subheader("The Chat History is")
for role, text in st.session_state['chat_history']:
    st.write(f"{role}: {text}")
