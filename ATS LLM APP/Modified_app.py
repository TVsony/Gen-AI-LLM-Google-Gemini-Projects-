import streamlit as st
import google.generativeai as genai
import os
import PyPDF2 as pdf
from dotenv import load_dotenv
import json

# Load environment variables from .env file
load_dotenv()

# Configure the Gemini API with the provided API key
genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

# Function to get a response from Gemini model based on the input prompt
def get_gemini_response(input):
    model = genai.GenerativeModel('gemini-pro')
    response = model.generate_content(input)
    return response.text

# Function to extract text from the uploaded PDF file (resume)
def input_pdf_text(uploaded_file):
    reader = pdf.PdfReader(uploaded_file)
    text = ""
    for page in range(len(reader.pages)):
        page = reader.pages[page]
        text += str(page.extract_text())
    return text

# Prompt template to be passed to the Gemini model for ATS evaluation
input_prompt = """
Hey Act Like a skilled or very experience ATS(Application Tracking System)
with a deep understanding of tech field,software engineering,data science ,data analyst
and big data engineer. Your task is to evaluate the resume based on the given job description.
You must consider the job market is very competitive and you should provide 
best assistance for improving the resumes. Assign the percentage Matching based 
on JD and
the missing keywords with high accuracy
resume:{text}
description:{jd}

I want the response in one single string having the structure
{{"JD Match":"%","MissingKeywords:[]","Profile Summary":""}}
"""

# Streamlit application setup
st.title("Smart ATS")
st.text("Improve Your Resume ATS")
jd = st.text_area("Paste the Job Description")  # Input area for Job Description
uploaded_file = st.file_uploader("Upload Your Resume", type="pdf", help="Please upload the PDF")  # File uploader for resume

# Button to submit and evaluate the resume
submit = st.button("Submit")

# If the submit button is clicked, evaluate the resume
if submit:
    if uploaded_file is not None:
        # Extract text from the uploaded PDF resume
        text = input_pdf_text(uploaded_file)

        # Format the prompt with the resume text and job description
        prompt_filled = input_prompt.format(text=text, jd=jd)
        
        # Call Gemini API to evaluate the resume
        response = get_gemini_response(prompt_filled)
        
        # Display the response from Gemini
        st.subheader("Evaluation Result")
        st.write(response)
    else:
        # Display a message if no file is uploaded
        st.write("Please upload a resume in PDF format.")
