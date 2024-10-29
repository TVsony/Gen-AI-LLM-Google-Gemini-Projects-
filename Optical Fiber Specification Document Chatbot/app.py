# Import necessary libraries
import streamlit as st
import os
from langchain_groq import ChatGroq
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.chains.combine_documents import create_stuff_documents_chain
from langchain_core.prompts import ChatPromptTemplate
from langchain.chains import create_retrieval_chain
from langchain_community.vectorstores import FAISS
from langchain_community.document_loaders import PyPDFDirectoryLoader
from langchain_google_genai import GoogleGenerativeAIEmbeddings
from dotenv import load_dotenv
import time

# Load environment variables
load_dotenv()
groq_api_key = os.getenv('GROQ_API_KEY')
os.environ["GOOGLE_API_KEY"] = os.getenv("GOOGLE_API_KEY")

# Streamlit app title
st.title("Gemma LLM Model Optical Fiber documents Specification Q/A chatbot")

# Initialize the ChatGroq LLM with an API key and model name
llm = ChatGroq(groq_api_key=groq_api_key, model_name="Llama3-8b-8192")

# Define the prompt template for answering questions
prompt = ChatPromptTemplate.from_template("""
Answer the questions based on the provided context only.
Please provide the most accurate response based on the question
<context>
{context}
<context>
Questions:{input}
""")

# Function to load and embed documents
def vector_embedding():
    if "vectors" not in st.session_state:  # Check if vector store is already created
        # Set up embeddings model
        st.session_state.embeddings = GoogleGenerativeAIEmbeddings(model="models/embedding-001")
        
        # Load PDFs from directory
        st.session_state.loader = PyPDFDirectoryLoader("./us_census")
        st.session_state.docs = st.session_state.loader.load()
        
        # Split documents into chunks
        st.session_state.text_splitter = RecursiveCharacterTextSplitter(chunk_size=1000, chunk_overlap=200)
        st.session_state.final_documents = st.session_state.text_splitter.split_documents(st.session_state.docs[:20])
        
        # Create FAISS vector store from documents
        st.session_state.vectors = FAISS.from_documents(st.session_state.final_documents, st.session_state.embeddings)

# User input for question
prompt1 = st.text_input("Enter Your Question From Documents")

# Button to embed documents
if st.button("Documents Embedding"):
    vector_embedding()  # Call function to create embeddings
    st.write("Vector Store DB Is Ready")

# Check for user input and process the question if entered
if prompt1:
    # Create a document chain and a retrieval chain
    document_chain = create_stuff_documents_chain(llm, prompt)
    retriever = st.session_state.vectors.as_retriever()
    retrieval_chain = create_retrieval_chain(retriever, document_chain)
    
    # Measure response time
    start = time.process_time()
    response = retrieval_chain.invoke({'input': prompt1})  # Run retrieval chain with user input
    print("Response time:", time.process_time() - start)
    
    # Display the answer
    st.write(response['answer'])
    
    # Streamlit expander to show context
    with st.expander("Document Similarity Search"):
        # Display relevant document chunks for context
        for i, doc in enumerate(response["context"]):
            st.write(doc.page_content)
            st.write("--------------------------------")
