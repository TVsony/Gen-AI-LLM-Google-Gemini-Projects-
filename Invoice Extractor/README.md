### MultiLanguage Invoice Extractor Application
This project is a Streamlit-based application that utilizes Google Gemini’s Generative AI capabilities to analyze invoice images and extract relevant information. Designed to support multilingual invoices, this app uses advanced image recognition and language processing to answer user-specific questions based on invoice data.

**Features**

- Invoice Extraction: Upload an invoice image, and the app can interpret and extract essential information.
- Multi-Language Support: Supports invoices in various languages, leveraging Google Gemini’s language models.
- Interactive Interface: Streamlit provides an interactive, user-friendly interface for uploading images and inputting queries.
- Customizable Input Prompt: Allows users to specify custom input for specific invoice analysis requirements.
- Configurable API Key: Securely configures the Google Gemini API key using environment variables for seamless integration.

**Technologies Used**
- Python 
- Streamlit: For interactive UI and user experience
- Pillow (PIL): For image processing and manipulation
- Google Generative AI (Gemini): Used for language understanding and vision capabilities
- dotenv: To securely manage environment variables for the API key
**Prerequisites**
- Python 3.10 or later
- Google Gemini API Key: Ensure you have access to Google’s Generative AI services.

**Set Up Environment Variables:**

Create a .env file in the root directory and add your Google API key:

GOOGLE_API_KEY=your_google_api_key

**Install Dependencies:**

pip install -r requirements.txt

**Run the Application:**

streamlit run app.py


**Usage**
Upload and Analyze Invoice:
- Open the application in your browser.
- Upload an invoice image (JPEG or PNG).
- Enter a specific query related to the invoice.
- Click on "Tell me about the Invoice" to receive AI-generated insights.

## Code Overview

**File Structure**
- app.py: Main application file containing Streamlit code, functions to process image and text input, and API requests.
- .env: Holds environment variables for secure storage of sensitive information.
- requirements.txt: Lists all Python dependencies.

**Future Improvements**
- Additional Language Support: Enhance the app’s ability to interpret and - - respond to invoices in a broader range of languages.
- Enhanced Querying: Enable more complex querying for detailed invoice data extraction.
- Export Options: Allow users to export extracted data in JSON or CSV format.