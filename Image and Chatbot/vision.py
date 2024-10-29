# Import necessary libraries
from dotenv import load_dotenv  # For loading environment variables
import streamlit as st  # Streamlit for web interface
import os  # For environment variable management
from PIL import Image  # For image processing
import google.generativeai as genai  # For Google Gemini API interactions

# Load environment variables from .env file
load_dotenv()

# Configure the Google Gemini API client with the API key from environment variables
genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

# Function to generate a response from the Gemini model based on text and/or image
def get_gemini_response(input, image):
    # Initialize the Gemini model for vision-based tasks
    model = genai.GenerativeModel("gemini-1.5-flash")
    
    # Check if there's a text input prompt, then generate content using both text and image
    if input != "":
        response = model.generate_content([input, image])
    else:
        # If only an image is provided, generate content using just the image
        response = model.generate_content(image)
    
    # Return the generated text response
    return response.text

# Set up the Streamlit app interface
st.set_page_config(page_title="Gemini Image Demo")  # Set the page title
st.header("Gemini Application")  # Display the header for the app

# Input field for user to enter a text prompt
input = st.text_input("Input Prompt: ", key="input")

# File uploader for the user to upload an image
uploaded_file = st.file_uploader("Choose an image...", type=["jpg", "jpeg", "png"])

# Initialize the image variable
image = ""

# If an image file is uploaded, open it and display it on the app interface
if uploaded_file is not None:
    image = Image.open(uploaded_file)  # Open the image
    st.image(image, caption="Uploaded Image.", use_column_width=True)  # Display the image

# Button to submit the input and generate a response
submit = st.button("Tell me about the image")

# If the submit button is clicked, generate and display the response
if submit:
    response = get_gemini_response(input, image)  # Get the response from Gemini model
    st.subheader("The Response is")  # Subheader for the response
    st.write(response)  # Display the response text