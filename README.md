## YT-RAGSense
A lightweight, production-ready Retrieval-Augmented Generation (RAG) system built using Typesense, FAISS, LangChain, and Groq LLMs.
This project allows you to index YouTube transcripts, documents, or custom datasets and query them using a fast vector search pipeline.

## 🚀 Features

 - High-speed vector search using Typesense / FAISS

 - LLM-powered answers using Groq API (Llama 3.1 / Mixtral)

 - Automatic text splitting and embedding

 - Supports JSONL, text files, PDFs, or custom loaders

 - Real-time query responses

 - Modular design (clean src/ folder architecture)

## 🏗️ Project Structure
# YT-RAGSense/
# │
# ├── data/                 # Raw input data (transcripts, docs, etc.)
# ├── faiss_store/          # Vector index (FAISS)
# ├── notebook/             # Notebooks for testing
# ├── src/
# │   ├── loaders/          # Data loading functions
# │   ├── embedding/        # Embedding pipeline
# │   ├── vectorstore/      # Typesense / FAISS wrappers
# │   ├── llm/              # Groq LLM wrapper
# │   └── rag_pipeline.py   # Main RAG workflow
# │
# ├── app.py                # Main app runner
# ├── main.py               # Example script
# ├── books.jsonl           # Sample dataset
# ├── requirements.txt      # Dependencies
# ├── pyproject.toml        # Poetry config (optional)
# └── README.md

##  Installation
 # 1. Clone the repo
 git clone https://github.com/Sathya-2006/YT-RAGSense.git
 cd YT-RAGSense

 # 2. Create virtual environment
 uv venv
.venv\Scripts\activate

 # 3.Install dependencies
 uv pip install -r requirements.txt

 # Environment Variables
 GROQ_API_KEY=your_api_key_here
 TYPESENSE_API_KEY=your_typesense_key
 TYPESENSE_HOST=ziktplh30uqsjbw6p-1.a1.typesense.net
 TYPESENSE_PORT=443
 TYPESENSE_PROTOCOL=https

## Build Vector Store
Run embedding + indexing:
   python app.py

## Run a Query
python main.py

Inside script:

from src.rag_pipeline import ask_rag
response = ask_rag("What is Generative AI?")
print(response)



