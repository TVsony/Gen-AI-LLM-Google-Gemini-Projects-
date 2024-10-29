# Import necessary libraries
import streamlit as st
from dotenv import load_dotenv
import os
import google.generativeai as genai
from youtube_transcript_api import YouTubeTranscriptApi

# Load environment variables (API keys, etc.)
load_dotenv()  # Loads all environment variables from the .env file

# Configure Google Gemini Pro with the API key
genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

# Prompt template to instruct Gemini to generate a summary
prompt = """
You are a YouTube video summarizer. Your task is to take the transcript text of the video
and summarize the key points in concise bullet points within 250 words.
Provide the summary of the following text: 
"""

# Define a function to extract transcript details from YouTube videos
def extract_transcript_details(youtube_video_url):
    """
    Extracts the transcript from a YouTube video using the video URL.
    Returns the transcript text as a single concatenated string.
    """
    try:
        # Parse video ID from URL (assuming standard format)
        video_id = youtube_video_url.split("=")[1]
        
        # Fetch the transcript using YouTubeTranscriptApi
        transcript_data = YouTubeTranscriptApi.get_transcript(video_id)

        # Concatenate all segments of the transcript into a single string
        transcript = ""
        for segment in transcript_data:
            transcript += " " + segment["text"]

        return transcript

    except Exception as e:
        raise e  # Raise any exceptions encountered (e.g., video has no transcript)

# Define a function to generate a summary based on the transcript
def generate_gemini_content(transcript_text, prompt):
    """
    Uses the Gemini Pro model to generate a concise summary of the transcript.
    """
    # Load and configure the model
    model = genai.GenerativeModel("gemini-pro")
    
    # Generate the summary by providing the prompt and transcript
    response = model.generate_content(prompt + transcript_text)
    return response.text

# Streamlit Application Layout

# Set up the title of the app
st.title("YouTube Transcript to Detailed Notes Converter")

# Input for YouTube video link
youtube_link = st.text_input("Enter YouTube Video Link:")

# Display video thumbnail if a link is provided
if youtube_link:
    # Extract video ID for thumbnail display
    video_id = youtube_link.split("=")[1]
    # Display the video thumbnail from YouTube
    st.image(f"http://img.youtube.com/vi/{video_id}/0.jpg", use_column_width=True)

# Button to generate detailed notes
if st.button("Get Detailed Notes"):
    # Extract the transcript from the video URL
    transcript_text = extract_transcript_details(youtube_link)

    # Check if transcript extraction was successful
    if transcript_text:
        # Generate a summary using the Gemini model
        summary = generate_gemini_content(transcript_text, prompt)
        
        # Display the summary in the Streamlit app
        st.markdown("## Detailed Notes:")
        st.write(summary)

