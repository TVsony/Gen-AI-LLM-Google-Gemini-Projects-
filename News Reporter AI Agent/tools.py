from dotenv import load_dotenv
import os
from crewai_tools import SuperDevTool

# Load environment variables from the .env file
load_dotenv()

# Retrieve SERPER API key from environment
serper_api_key = os.getenv('SERPER_API_KEY')
if not serper_api_key:
    raise ValueError("SERPER_API_KEY is not set in environment variables.")

# Initialize the tool for internet searching capabilities
tool = SuperDevTool(api_key=serper_api_key)


