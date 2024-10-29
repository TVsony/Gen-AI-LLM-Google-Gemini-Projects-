# Importing necessary libraries
from dotenv import load_dotenv  # To load environment variables from a .env file
import base64  # For encoding images to base64
import streamlit as st  # For creating the web application interface
import os  # For accessing environment variables and file paths
import io  # For handling byte streams
from PIL import Image  # For image processing
import pdf2image  # For converting PDF files to images
import google.generativeai as genai  # For interacting with Google's generative AI model

# Load environment variables (like API keys) from .env file
load_dotenv()
# Configure the generative AI model with the API key
genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

# Function to get a response from the Gemini model
def get_gemini_response(input, pdf_content, prompt):
    # Create an instance of the generative model
    model = genai.GenerativeModel('gemini-1.5-flash')
    # Generate content using the model with the provided input and PDF content
    response = model.generate_content([input, pdf_content[0], prompt])
    return response.text  # Return the generated response text

# Function to process the uploaded PDF and convert it to an image
def input_pdf_setup(uploaded_file):
    if uploaded_file is not None:
        # Convert the uploaded PDF file to images
        images = pdf2image.convert_from_bytes(uploaded_file.read())
        first_page = images[0]  # Get the first page of the PDF

        # Convert the first page image to bytes
        img_byte_arr = io.BytesIO()  # Create a byte stream
        first_page.save(img_byte_arr, format='JPEG')  # Save image as JPEG
        img_byte_arr = img_byte_arr.getvalue()  # Get the byte value of the image

        # Prepare the PDF parts for the AI model
        pdf_parts = [
            {
                "mime_type": "image/jpeg",  # Specify the MIME type
                "data": base64.b64encode(img_byte_arr).decode()  # Encode the image to base64
            }
        ]
        return pdf_parts  # Return the processed PDF parts
    else:
        raise FileNotFoundError("No file uploaded")  # Raise an error if no file is uploaded

# Streamlit App Setup
st.set_page_config(page_title="ATS Resume Expert")  # Set the title of the app
st.header("ATS Tracking System")  # Add a header to the app
input_text = st.text_area("Job Description: ", key="input")  # Text area for job description input
uploaded_file = st.file_uploader("Upload your resume (PDF)...", type=["pdf"])  # File uploader for PDF resumes

# Check if a file has been uploaded
if uploaded_file is not None:
    st.write("PDF Uploaded Successfully")  # Notify user of successful upload

# Define buttons for user actions
submit1 = st.button("Tell Me About the Resume")  # Button to analyze resume
submit2 = st.button("Percentage match")  # Button to check percentage match

# Prompts for AI model based on user actions
input_prompt1 = """
You are an experienced HR With Tech Experiance in thefield of Data Science,Full Stack Web development,Big Data Engineering,DEVOPS,Data Analyst,  your task is to review the provided resume against the job description. Please share your professional evaluation on whether the candidate's profile aligns with the role. Highlight the strengths and weaknesses of the applicant in relation to the specified job requirements.
"""

input_prompt2 = """
You are a skilled ATS (Applicant Tracking System) scanner with a deep understanding of data science and ATS functionality,your task is to evaluate the resume against the provided job description. Give me the percentage of match if the resume matches the job description. First the output should come as percentage and then keywords missing and last final thoughts.
"""

# Logic for the "Tell Me About the Resume" button
if submit1:
    if uploaded_file is not None:
        pdf_content = input_pdf_setup(uploaded_file)  # Process the uploaded PDF
        response = get_gemini_response(input_prompt1, pdf_content, input_text)  # Get response from AI
        st.subheader("The Response is")  # Subheader for the response section
        st.write(response)  # Display the AI's response
    else:
        st.write("Please upload the resume")  # Prompt if no resume is uploaded

# Logic for the "Percentage match" button
elif submit2:
    if uploaded_file is not None:
        pdf_content = input_pdf_setup(uploaded_file)  # Process the uploaded PDF
        response = get_gemini_response(input_prompt2, pdf_content, input_text)  # Get response from AI
        st.subheader("The response is")  # Subheader for the response section
        st.write(response)  # Display the AI's response
    else:
        st.write("Please upload the resume")  # Prompt if no resume is uploaded
