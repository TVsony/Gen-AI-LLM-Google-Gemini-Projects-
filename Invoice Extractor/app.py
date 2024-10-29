# Load environment variables from the .env file
from dotenv import load_dotenv 
load_dotenv()  # Load environment variables

# Import necessary libraries
import streamlit as st
import os
import pathlib
import textwrap
from PIL import Image
import google.generativeai as genai

# Configure Google Gemini API with the API key from environment variables
os.getenv("GOOGLE_API_KEY")  # Retrieve the Google API key
genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))  # Configure the API

# Define a function to generate responses from the Gemini model
def get_gemini_response(input, image, prompt):
    model = genai.GenerativeModel('gemini-1.5-flash')  # Initialize the model for vision tasks
    response = model.generate_content([input, image[0], prompt])  # Generate content based on input and image
    return response.text  # Return the response text

# Define a function to set up the uploaded image
def input_image_details(uploaded_file):
    # Check if a file has been uploaded
    if uploaded_file is not None:
        bytes_data = uploaded_file.getvalue()  # Read the file into bytes
        image_parts = [
            {
                "mime_type": uploaded_file.type,  # Get the MIME type of the uploaded file
                "data": bytes_data  # Store the image data
            }
        ]
        return image_parts  # Return the image parts
    else:
        raise FileNotFoundError("No file uploaded")  # Raise an error if no file is uploaded

# Initialize the Streamlit app
st.set_page_config(page_title="Gemini Image Demo")  # Set the page title
st.header("MultiLanguage Invoice Extractor Application")  # Display the header

# Create an input text field for the user
input = st.text_input("Input Prompt: ", key="input")  # Text input for user prompt
uploaded_file = st.file_uploader("Choose an image...", type=["jpg", "jpeg", "png"])  # File uploader for images
image = ""  # Initialize the image variable

# If an image file is uploaded, open and display it
if uploaded_file is not None:
    image = Image.open(uploaded_file)  # Open the uploaded image
    st.image(image, caption="Uploaded Image.", use_column_width=True)  # Display the image

# Create a submit button for user interaction
submit = st.button("Tell me about the Invoice")  # Button to submit the input

# Define an input prompt for the model
input_prompt = """
               You are an expert in understanding invoices.
               You will receive input images as invoices &
               you will have to answer questions based on the input image
               """

# If the submit button is clicked
if submit:
    image_data = input_image_details(uploaded_file)  # Process the uploaded image
    response = get_gemini_response(input_prompt, image_data, input)  # Get the response from the model
    st.subheader("The response is")  # Display subheader for the response
    st.write(response)  # Output the model's response
