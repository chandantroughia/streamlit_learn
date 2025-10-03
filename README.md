# Streamlit Learning Projects

This repository contains Streamlit applications demonstrating AI-powered features using Google's Gemini API and LangChain.

## Project Structure
```
streamlit_learn/
├── notebooks/
│   ├── assignment1_visual_qa.ipynb      # Visual Q&A notebook
│   ├── assignment2_rag_pdf.ipynb        # RAG PDF notebook
│   ├── app_visual_qa.py                 # Visual Q&A Streamlit app
│   └── app_rag_pdf.py                   # RAG PDF Streamlit app
├── requirements.txt                      # Python dependencies
├── .env                                  # Environment variables (not in git)
└── README.md                             # This file
```
## Applications

### 1. Visual Q&A Bot (`app_visual_qa.py`)
An interactive chatbot that answers questions about uploaded images using Google's Gemini Vision model.

**Features:**
- Upload images (JPG, JPEG, PNG)
- Ask questions about the uploaded image
- Chat history with conversation context
- Real-time responses using Gemini 2.5 Flash

**Screenshot:**
![Visual QA Screenshot](QA_ScreenShot.png)

### 2. RAG PDF Bot (`app_rag_pdf.py`)
A Retrieval-Augmented Generation (RAG) chatbot that answers questions based on uploaded PDF documents.

**Features:**
- Upload PDF documents
- Automatic text extraction and vectorization
- Semantic search using ChromaDB
- Context-aware responses using LangChain
- Chat history and conversation memory

**Screenshots:**
![RAG Screenshot 1](rag_1.png)
![RAG Screenshot 2](rag_2.png)

## Notebooks

### `assignment1_visual_qa.ipynb`
Jupyter notebook exploring visual question answering with Gemini Vision API. Demonstrates:
- Image encoding and processing
- Multimodal prompts with text and images
- Response generation

### `assignment2_rag_pdf.ipynb`
Jupyter notebook implementing RAG pipeline for PDF documents. Covers:
- PDF text extraction using PyMuPDF
- Text chunking and embedding
- Vector store creation with ChromaDB
- Retrieval and generation workflow

## Setup

### Prerequisites
- Python 3.8+
- Google Gemini API key

### Installation

1. **Clone the repository:**
   ```bash
   git clone <repository-url>
   cd streamlit_learn
   ```

2. **Create a virtual environment:**
   ```bash
   python -m venv .venv
   source .venv/bin/activate  # On Windows: .venv\Scripts\activate
   ```

3. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

4. **Set up environment variables:**
   Create a `.env` file in the root directory:
   ```env
   GEMINI_API_KEY=your_gemini_api_key_here
   ```

   Get your API key from: https://makersuite.google.com/app/apikey

## Running the Applications

### Visual Q&A Bot
```bash
cd notebooks
streamlit run app_visual_qa.py
```

The app will open in your browser at `http://localhost:8501`

**Usage:**
1. The chat interface appears first
2. Upload an image using the file uploader
3. Ask questions about the image in the chat box
4. View responses in real-time

### RAG PDF Bot
```bash
cd notebooks
streamlit run app_rag_pdf.py
```

The app will open in your browser at `http://localhost:8501`

**Usage:**
1. Upload a PDF document
2. Wait for the document to be processed
3. Ask questions about the document content
4. Get accurate answers based on the PDF content

## Running Notebooks

Launch Jupyter:
```bash
jupyter notebook
```

Navigate to the `notebooks/` directory and open the desired notebook.

## Dependencies

- **streamlit**: Web application framework
- **google-generativeai**: Google Gemini API client
- **langchain**: LLM application framework
- **langchain-google-genai**: LangChain integration for Gemini
- **langchain-community**: Community integrations for LangChain
- **langchain-chroma**: ChromaDB vector store integration
- **python-dotenv**: Environment variable management
- **Pillow**: Image processing
- **pymupdf**: PDF text extraction
- **pandas**: Data manipulation

## Configuration

Both applications use the following configuration:
- **Model**: `gemini-2.5-flash`
- **Temperature**: 0.3 (for consistent responses)
- **Vector Store**: ChromaDB (for RAG application)

## Notes

- The `.gitignore` excludes `.env`, `chroma_db/`, and other sensitive files
- Chat history is maintained in session state
- Vector databases are stored locally in `chroma_db/`
- For better performance, install Watchdog: `pip install watchdog`

## Contributing

Feel free to open issues or submit pull requests for improvements!

## License

This project is for educational purposes.
