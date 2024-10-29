# Project: Chat with Multiple PDF Documents using Google Gemini

**Project Overview**

- This project is a Streamlit-based application that enables interactive querying of content from multiple PDF documents.
- By combining PDF text extraction, vector-based search, and Google Gemini's NLP capabilities, the app allows users to ask questions based on uploaded PDF content and receive context-aware responses.

**Problem Statement**
- Often, it’s challenging to sift through multiple lengthy PDF documents to find specific information quickly.
- Traditional search methods may lack contextual understanding, making it difficult to answer questions based on combined content from multiple documents.

**Project Goal**

- To create an intelligent, conversational interface for users to interact with content from multiple PDFs, facilitating quick and accurate answers to document-based questions.

**Steps and Solution**

1. **Text Extraction:** Extract text from each page of uploaded PDF documents using PyPDF2.
2. **Text Chunking:** Split the extracted text into manageable chunks for better processing and embedding.
3. **Embedding with Google Gemini:** Use Google Generative AI embeddings to create vector representations of the text chunks for effective similarity search.
4. **FAISS Vector Storage:** Store the text embeddings using FAISS for fast, similarity-based retrieval of relevant chunks.
5. **Conversational Chain Setup:** Define a prompt-based conversational chain using LangChain and Google Gemini, ensuring responses are accurate and context-aware.
6. **Querying:** Accept user questions, retrieve relevant document chunks based on similarity, and generate detailed answers using Google Gemini’s language model.

**Dependencies**

- streamlit
- PyPDF2
- langchain
- google-generativeai
- faiss-cpu
- langchain-google-genai
- dotenv

**Code Explanation**

- Text Extraction (get_pdf_text): Reads all uploaded PDFs and extracts text from each page.
- Text Chunking (get_text_chunks): Splits the extracted text into chunks for efficient processing.
- Vector Store Creation (get_vector_store): Uses Google Gemini embeddings to create a FAISS vector store of document chunks.
- Conversational Chain (get_conversational_chain): Loads a LangChain question-answering model using Google Gemini.
- User Query (user_input): Retrieves similar text chunks based on user questions and generates answers using the conversational model.


**Usage**

- **Upload PDFs:** Use the sidebar to upload one or multiple PDF files.

- **Process Files:** Click on "Submit & Process" to extract and store text embeddings.

- **Ask Questions:** Enter a question in the main input field to query the uploaded documents. The application will retrieve relevant information and respond based on the context of the PDF content.

**Project Impact**

1. **Improved Efficiency:** Enables faster retrieval of document-specific information, enhancing productivity in document-heavy environments.

2. **Enhanced Contextual Search:** Provides answers based on the entire content of multiple documents, increasing search accuracy.

3. **User-Friendly Interface:** Allows non-technical users to ask questions and interact with PDF content seamlessly through a simple web interface.
