
# YouTube Transcript to Detailed Notes Converter

## Project Overview

The **YouTube Transcript to Detailed Notes Converter** is a web application designed to help users quickly understand the content of YouTube videos by summarizing their transcripts. Using Google’s Gemini Pro generative model, the app extracts key information from the transcript and presents it in concise, bullet-point notes. This tool is ideal for anyone looking to save time by reading a brief summary of a video's content rather than watching the entire video.

## Project Goal

The goal of this project is to automate the process of generating summaries for YouTube videos using AI. By simply inputting a YouTube video link, users can obtain a clear, point-form summary of the video, which is especially useful for long or educational videos.

## Problem Statement

With the sheer volume of video content available on platforms like YouTube, it can be challenging and time-consuming for users to watch every video in detail. This application addresses the need for a quick and efficient method to consume video content by converting the video transcript into a summary, allowing users to grasp the essential information in a fraction of the time.

## Key Features

- **Automated Transcript Retrieval**: Extracts the transcript of any video directly from YouTube.
- **AI-Powered Summarization**: Uses Google Gemini Pro to summarize the transcript text effectively.
- **Concise Bullet Points**: Summarized content is displayed in clear, point-form notes.
- **Interactive Web Interface**: Built with Streamlit, the app is user-friendly and visually appealing.


## Technologies Used

- **Python**: Core language for backend development.
- **Streamlit**: For creating the interactive web interface.
- **YouTubeTranscriptAPI**: To fetch transcripts from YouTube videos.
- **Google Gemini Pro**: For generating summaries from the video transcript.
- **Dotenv**: For secure handling of API keys and environment variables.

2. **Create a Virtual Environment**

3. **Install Dependencies**

4. **Set Up Environment Variables**

5. **Run the Application**

#### Explanation of Each Section:
1. Imports:

- Libraries like streamlit, dotenv, and google.generativeai for the app interface, environment management, and text generation respectively.
- YouTubeTranscriptApi is used for retrieving video transcripts.

2. **Load Environment Variables:**

- The load_dotenv() function loads API keys and other secrets from a .env file, keeping sensitive data secure.

3. **Configuration:**

The Google Gemini Pro model is configured with the API key using genai.configure().
4. **Prompt Template:**

- A predefined prompt variable guides the Gemini Pro model to create a concise summary of the transcript.

5. **Extracting Transcript Function:**

- extract_transcript_details function takes a YouTube URL and extracts the video ID.
- Uses the YouTube API to retrieve the transcript and concatenates it into a single string.

6. **Generating Summary Function:**

- generate_gemini_content sends the transcript text to the Gemini model with a summarization prompt.
- The generated summary is returned as a response.text.

7. **Streamlit App Layout:**

- App Title: Sets up the title with st.title.
- Input Box for YouTube Link: Accepts a YouTube video URL.
- Thumbnail Display: Shows the video thumbnail using the video ID extracted from the URL.
- Get Notes Button: When clicked, it triggers transcript extraction and summarization.
- Summary Display: Shows the final summary under a "Detailed Notes" section.

## Usage

1. Open the app in your web browser
2. Enter the YouTube video link in the provided input box.
3. Click on the "Get Detailed Notes" button to fetch the transcript and generate the summary.
4. The app will display the video thumbnail and the summary in concise bullet points.

## Example Workflow

1. **Input**: You enter a YouTube link for a video.
2. **Transcript Extraction**: The app fetches the transcript of the video using the YouTubeTranscriptAPI.
3. **AI Summarization**: Google Gemini Pro processes the transcript to generate a summary.
4. **Output**: The app displays the summary in clear, easy-to-read points.

## Project Structure

├── app.py                 # Main application code
├── requirements.txt       # Python dependencies
├── .env                   # Environment variables file (API keys)
└── README.md              # Project documentation

**Future Improvements**

- Multi-language Support: Allow summarization of videos in multiple languages.
- Enhanced Summarization Options: Offer users options to control summary length and level of detail.
- Extended Transcript Options: Enable users to edit transcripts for accuracy before summarization.

**Acknowledgments** 
- Thanks to Krish Naik sir sharing amazing his knowlege.
- Streamlit for the user-frendly web app framework.
- Youtube Transcript API for easy access to video transcript.

