# Health Management APP

# Load environment variables from .env file
from dotenv import load_dotenv
load_dotenv()  # This loads environment variables from a .env file, allowing access to sensitive data like API keys.

import streamlit as st
import os
import google.generativeai as genai  # Import the Google Generative AI library for AI responses
from PIL import Image  # Import Image class from Pillow for image handling

# Configure Google Gemini with API key from environment variables
genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

## Function to load Google Gemini Pro Vision API and get response
def get_gemini_repsonse(input, image, prompt):
    # Create a GenerativeModel instance for 'gemini-pro-vision'
    model = genai.GenerativeModel('gemini-1.5-pro')
    # Generate content using the provided input, image, and prompt
    response = model.generate_content([input, image[0], prompt])
    return response.text  # Return the generated text response

# Function to handle the uploaded image
def input_image_setup(uploaded_file):
    # Check if a file has been uploaded
    if uploaded_file is not None:
        # Read the file into bytes
        bytes_data = uploaded_file.getvalue()

        # Prepare the image parts for processing
        image_parts = [
            {
                "mime_type": uploaded_file.type,  # Get the MIME type of the uploaded file
                "data": bytes_data  # The actual image data in bytes
            }
        ]
        return image_parts  # Return the prepared image data
    else:
        raise FileNotFoundError("No file uploaded")  # Raise an error if no file is uploaded

## Initialize the Streamlit app
st.set_page_config(page_title="Gemini Health App")  # Set the title of the web app

# Header for the app
st.header("Gemini Health App")

# Text input for the user to enter a prompt
input = st.text_input("Input Prompt: ", key="input")

# File uploader for the user to upload an image (JPG, JPEG, PNG formats)
uploaded_file = st.file_uploader("Choose an image...", type=["jpg", "jpeg", "png"])

# Variable to hold the uploaded image
image = ""   
if uploaded_file is not None:
    # Open the uploaded image using Pillow
    image = Image.open(uploaded_file)
    # Display the uploaded image on the app
    st.image(image, caption="Uploaded Image.", use_column_width=True)

# Button to submit the image and prompt for calorie calculation
submit = st.button("Tell me the total calories")

# Prompt for the Gemini model to calculate calories
input_prompt = """
Hey You are an expert in nutrition. Your task is to analyze the food items in the image
and calculate the total calories, also provide the details of every food item with calorie intake
in the following format:

1. Item 1 - no of calories
2. Item 2 - no of calories
----
----
"""

# If the submit button is clicked
if submit:
    # Prepare the uploaded image for processing
    image_data = input_image_setup(uploaded_file)
    # Call the function to get the response from the Gemini model
    response = get_gemini_repsonse(input_prompt, image_data, input)
    # Display the response from the AI in the app
    st.subheader("The Response is")
    st.write(response)  # Show the generated text response in the app

