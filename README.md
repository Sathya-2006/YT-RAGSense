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
YT-RAGSense/
│
├── data/                 # Raw input data (transcripts, docs, etc.)
├── faiss_store/          # Vector index (FAISS)
├── notebook/             # Notebooks for testing
├── src/
│   ├── loaders/          # Data loading functions
│   ├── embedding/        # Embedding pipeline
│   ├── vectorstore/      # Typesense / FAISS wrappers
│   ├── llm/              # Groq LLM wrapper
│   └── rag_pipeline.py   # Main RAG workflow
│
├── app.py                # Main app runner
├── main.py               # Example script
├── books.jsonl           # Sample dataset
├── requirements.txt      # Dependencies
├── pyproject.toml        # Poetry config (optional)
└── README.md

