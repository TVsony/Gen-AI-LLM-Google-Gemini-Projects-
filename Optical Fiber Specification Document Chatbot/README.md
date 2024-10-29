# Gemma Model Document Q&A

## Project Overview
The **Gemma Model Document Q&A** project is a web-based application that allows users to ask questions based on the contents of documents in PDF format. Powered by Groq's Llama model and Google’s Generative AI embeddings, this tool leverages LangChain and FAISS to create a semantic search and retrieval system. Users can ask questions directly, and the system will fetch the most relevant information from the documents and provide accurate, context-based answers.

## Project Goal
The main objective of this project is to create an interactive and efficient document question-answering system that:
1. Enables users to perform document-based queries effortlessly.
2. Provides reliable answers based on document content, ensuring accuracy and relevance.
3. Uses state-of-the-art embeddings and language models to facilitate fast and meaningful responses.

## Problem Statement
Many organizations and individuals handle large volumes of documents, which makes information retrieval challenging. Manually searching through documents is time-consuming and inefficient, especially when specific answers are needed from dense and lengthy texts. This project addresses the challenge by implementing a streamlined, AI-powered solution for document-based Q&A.

## Features
- **PDF Document Loading**: Loads all PDF documents from a specified directory and preprocesses them for querying.
- **Text Splitting and Embeddings**: Converts documents into smaller, manageable chunks and generates embeddings for efficient semantic search.
- **Vector Storage with FAISS**: Utilizes FAISS (Facebook AI Similarity Search) for fast similarity search and retrieval of relevant document sections.
- **Question-Answering with LLM**: Uses Groq's Llama language model to generate context-aware answers based on retrieved document sections.
- **Streamlit Interface**: A user-friendly web interface for document embedding, question input, and answer display.


## Technology Stack
- **Python**: Primary language for backend and application logic.
- **Streamlit**: Interactive web app framework for displaying and running the application.
- **LangChain**: Framework for building language model applications with components like retrieval chains and document splitting.
- **Groq**: Provides Groq-optimized models (like Llama) for handling large language model tasks.
- **FAISS**: Library for fast vector similarity search, crucial for embedding retrieval.
- **Google Cloud AI Platform**: Used for generating embeddings via Google’s Generative AI model.
- **dotenv**: Securely loads API keys and environment variables.

## File Structure

├── app.py                   # Main application script
├── us_census/               # Directory containing PDF files for ingestion
├── .env                     # Environment file for storing API keys
├── requirements.txt         # Python dependencies
└── README.md                # Project documentation


Set up API keys:
- Create a .env file in the root directory
- GROQ_API_KEY=your_groq_api_key
- GOOGLE_API_KEY=your_google_api_key

#### Project Requirements

Install dependencies: pip install -r requirements.txt


1 **faiss-cpu:** FAISS (Facebook AI Similarity Search) is a library optimized for efficient similarity search and clustering of dense vectors. The CPU version allows you to use FAISS on machines without a GPU, enabling efficient search in large collections of embeddings (useful in NLP and recommendation systems).

2 **groq:** Groq refers to both the hardware and software stack from Groq Inc., optimized for high-performance AI workloads, especially in inference. Groq software is typically used to work with Groq hardware, focusing on extremely low latency for model inference.

3 **langchain-groq:** This package is an integration of LangChain (a framework for building applications with LLMs) with Groq, allowing the deployment of LangChain-based apps on Groq's high-performance hardware for efficient processing of AI tasks.

4 **PyPDF2:** PyPDF2 is a Python library for working with PDF files. It can extract text, split and merge documents, and handle metadata, among other tasks. Commonly used for PDF processing in data pipelines and document management applications.

5 **langchain_google_genai:** This package integrates LangChain with Google’s GenAI services. It allows you to use Google’s Generative AI tools (e.g., language models and embedding services) within the LangChain framework, useful for building applications that leverage Google’s language capabilities.

6 **langchain:** LangChain is a popular framework for building applications powered by language models. It provides abstractions for working with LLMs, memory, chains, and tools, making it easier to create advanced applications like chatbots and generative tools.

7 **streamlit:** Streamlit is a Python library for building interactive web applications with minimal code, often used for data science and machine learning demos. It simplifies UI creation, making it popular for visualizing data and building dashboards quickly.

8 **langchain_community:** This package is likely an extension of LangChain, providing community-built integrations, tools, or enhancements to the core LangChain library. It can contain experimental or specialized tools and connectors.

9 **python-dotenv:** This library loads environment variables from a .env file into the system environment, useful for managing configuration settings like API keys and secrets in a secure and organized manner.

10 **pypdf:** Like PyPDF2, pypdf is a library for handling PDF files. It can extract text, merge and split files, and handle PDF metadata. It's lightweight and suitable for document processing tasks in various applications.

11 **google-cloud-aiplatform (>=1.38):** This is Google Cloud’s AI Platform library, providing tools to work with Google’s Vertex AI services. Version 1.38 includes new or enhanced features, such as improved support for model training, deployment, and explanations (for instance, through SHAP values or integrated gradients), to interpret model predictions.

### Explanation Within Code Sections

1. **Imports and Environment Setup**

- Loads required libraries and environment variables to access API keys.

2. **LLM and Prompt Initialization**

- ChatGroq is set up to use the Llama3-8b-8192 model.
- ChatPromptTemplate defines how the model should respond, including instructions and placeholders for context and input.

3. **vector_embedding Function**

- Checks if vectors are already in session state to avoid reloading.
- Loads and processes PDFs, creating embeddings using Google’s embedding-001 model.
- Splits documents into chunks and stores them in FAISS for efficient retrieval.

4. **User Input and Action Handling**

- Text input (prompt1) captures user questions.
- Button triggers vector_embedding, creating the vector store if not already done.

5. **Retrieval and Answer Display**

- Constructs a document_chain and retrieval_chain to search and generate an answer.
- Displays response time and answer in the Streamlit interface.
- st.expander reveals context documents related to the answer.

This structure provides a solid framework for processing user queries on document content and delivering contextual responses. Let me know if you'd like more details on any specific function or section!



## Start the Streamlit application

streamlit run app.py

## Load Documents

- Ensure your PDF documents are stored in the us_census directory.
- Click the "Documents Embedding" button in the app to load and process documents.

**Ask Questions**

- Enter a question in the text input field and click to retrieve an answer.
- The response, along with relevant context, will display on the screen.

### Explanation of Key Components

1. **Document Embedding**

The vector_embedding function processes the documents by

- Loading PDF documents and extracting text.
- Splitting text into manageable chunks.
- Creating vector embeddings using Google’s Generative AI model.
- Storing embeddings in FAISS for fast similarity search.

2. **Question-Answering Pipeline**

- Retrieval Chain: Retrieves the most relevant document chunks based on similarity to the input question.
- Document Chain: Processes the retrieved text and generates an answer using the Groq language model.

3. **User Interface**

- Simple, intuitive interface built with Streamlit.
- Allows users to load documents, ask questions, and see results in one place.

4. **Future Improvements**

- **Support for Additional Document Types:** Extend beyond PDF to support Word and text files.
- **Advanced Filtering:** Allow users to filter answers by document name, date, or other metadata.
- **Response Optimization:** Reduce response time by implementing caching and parallel processing.