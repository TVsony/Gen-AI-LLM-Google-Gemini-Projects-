# Import required libraries
import streamlit as st
from PyPDF2 import PdfReader  # Library for reading PDF files
from langchain.text_splitter import RecursiveCharacterTextSplitter  # Text splitter for handling long texts
import os
from langchain_google_genai import GoogleGenerativeAIEmbeddings  # Google Generative AI Embeddings for semantic search
import google.generativeai as genai  # Google Generative AI library
from langchain.vectorstores import FAISS  # FAISS for vector store and similarity search
from langchain_google_genai import ChatGoogleGenerativeAI  # Google Generative AI for conversational chat
from langchain.chains.question_answering import load_qa_chain  # Chain for QA tasks
from langchain.prompts import PromptTemplate  # Template for prompt customization
from dotenv import load_dotenv  # Load environment variables from a .env file

# Load environment variables (such as API keys) from a .env file
load_dotenv()
os.getenv("GOOGLE_API_KEY")
genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))  # Set up Google Generative AI with API key

# Function to extract text from uploaded PDF files
def get_pdf_text(pdf_docs):
    text = ""
    # Loop through each PDF file
    for pdf in pdf_docs:
        pdf_reader = PdfReader(pdf)
        # Loop through each page and extract text
        for page in pdf_reader.pages:
            text += page.extract_text()
    return text

# Function to split extracted text into smaller chunks for efficient processing
def get_text_chunks(text):
    # Chunk size is set to 10,000 characters with 1,000 characters overlap
    text_splitter = RecursiveCharacterTextSplitter(chunk_size=10000, chunk_overlap=1000)
    chunks = text_splitter.split_text(text)
    return chunks

# Function to create and save a FAISS vector store from text chunks
def get_vector_store(text_chunks):
    # Initialize embeddings with Google’s embedding model
    embeddings = GoogleGenerativeAIEmbeddings(model="models/embedding-001")
    # Generate vector store from text chunks
    vector_store = FAISS.from_texts(text_chunks, embedding=embeddings)
    vector_store.save_local("faiss_index")  # Save the vector store locally

# Function to set up a conversational QA chain with Google Generative AI model
def get_conversational_chain():
    # Define the prompt template
    prompt_template = """
    Answer the question as detailed as possible from the provided context. 
    Make sure to provide all details. If the answer is not in the provided context, say, 
    'answer is not available in the context,' and do not provide a wrong answer.\n\n
    Context:\n {context}?\n
    Question: \n{question}\n
    Answer:
    """
    
    # Configure the conversational AI model with a low temperature for focused responses
    model = ChatGoogleGenerativeAI(model="gemini-pro", temperature=0.3)
    # Set up the prompt for the QA chain
    prompt = PromptTemplate(template=prompt_template, input_variables=["context", "question"])
    # Load the QA chain with the specified prompt and model
    chain = load_qa_chain(model, chain_type="stuff", prompt=prompt)
    return chain

# Function to process user questions and fetch relevant answers
def user_input(user_question):
    embeddings = GoogleGenerativeAIEmbeddings(model="models/embedding-001")
    
    # Load the vector store with safe deserialization enabled
    new_db = FAISS.load_local("faiss_index", embeddings, allow_dangerous_deserialization=True)
    
    # Perform similarity search to retrieve relevant document chunks
    docs = new_db.similarity_search(user_question)

    # Get the conversational QA chain
    chain = get_conversational_chain()
    
    # Pass documents and question to the chain, receive response
    response = chain(
        {"input_documents": docs, "question": user_question}, return_only_outputs=True)
    
    # Display response in Streamlit app
    st.write("Reply: ", response["output_text"])

# Main function to set up the Streamlit application
def main():
    # Configure Streamlit app settings
    st.set_page_config(page_title="Chat PDF")  # Set page title
    st.header("Chat with PDF using Gemini💁")  # Display header for app

    # User input field for asking questions
    user_question = st.text_input("Ask a Question from the PDF Files")

    # Process question if input is provided
    if user_question:
        user_input(user_question)

    # Sidebar setup for PDF upload
    with st.sidebar:
        st.title("Menu:")
        # File uploader to upload multiple PDF files
        pdf_docs = st.file_uploader("Upload your PDF Files and Click on the Submit & Process Button", accept_multiple_files=True)
        if st.button("Submit & Process"):
            with st.spinner("Processing..."):
                # Extract and process text from uploaded PDFs
                raw_text = get_pdf_text(pdf_docs)
                text_chunks = get_text_chunks(raw_text)
                # Create vector store for similarity search
                get_vector_store(text_chunks)
                st.success("Done")

# Execute the main function when running the script
if __name__ == "__main__":
    main()




