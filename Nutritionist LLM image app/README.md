# Gemini Health Management App

## Project Overview
The **Gemini Health Management App** is a web-based application developed using Streamlit that utilizes Google’s Gemini Pro Vision API to analyze food items in images. The app provides users with nutritional information, specifically the total calorie count and details of each food item identified within an uploaded image. This tool is aimed at helping users make informed dietary choices by understanding the caloric intake of their meals.

## Project Goal
The primary goal of the Gemini Health Management App is to empower users with the knowledge of their dietary habits through the analysis of food images. By leveraging advanced generative AI technology, the app aims to:
- Provide accurate calorie counts for various food items in a user-friendly interface.
- Offer detailed insights into individual food items and their caloric contributions.
- Enhance user engagement with interactive features and instant feedback.

## Problem Statement
In today’s fast-paced world, many individuals struggle to maintain a balanced diet and often lack accurate information regarding the caloric content of the foods they consume. This can lead to unhealthy eating habits and weight management challenges. The **Gemini Health Management App** addresses this issue by:
- Allowing users to upload images of their meals.
- Using AI technology to analyze the food items and calculate their total caloric intake.
- Presenting this information in an easily understandable format.

## Features
- **User-Friendly Interface**: Intuitive design allowing easy navigation and interaction.
- **Image Upload**: Users can upload food images in JPG, JPEG, or PNG formats.
- **Caloric Analysis**: The app provides detailed caloric information for each food item detected in the uploaded image.
- **Generative AI Integration**: Utilizes the Google Gemini Pro Vision API to accurately identify food items and calculate calories.
- **Instant Feedback**: Users receive immediate results upon submission.

## Technologies Used
- **Streamlit**: A Python library for building interactive web applications.
- **Google Generative AI**: For analyzing food images and generating responses.
- **Pillow (PIL)**: For image processing and manipulation.
- **Python Dotenv**: To manage environment variables securely.

## Getting Started

### Prerequisites
- Python 3.10 or higher
- Google API Key (for accessing the Gemini Pro Vision API)
- Necessary libraries as specified in `requirements.txt`

**Create and activate a virtual environment**

conda create -p venv python==3.10 -y
conda activate venv/

**Install the required packages**

pip install -r requirements.txt

**Set up your Google API key**

GOOGLE_API_KEY=your_api_key_here

**Run the Streamlit app**

streamlit run app.py

### Usage
- Navigate to the app in your web browser.
- Input a prompt in the text area if desired.
- Upload an image of your food item(s).
- Click the "Tell me the total calories" button to receive analysis.
- View the results displayed below the upload section.

**Acknowledgments**
- Thanks to Krish Sir making and sharing such wonderful knowlege 
- Thanks to Streamlit for providing a fantastic platform for building web apps.
- Special thanks to the Google Generative AI team for their amazing API that powers this app.