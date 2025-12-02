# **YT-RAGSense**

A modular, blazing-fast Retrieval-Augmented Generation (RAG) system powered by:

- Groq LLMs (Llama 3.x, Mixtral)

- Typesense / FAISS vector stores

- LangChain Community

- HuggingFace Embeddings

Built for developers who want a clean, production-ready RAG pipeline for YouTube transcripts, documents, or any custom dataset.


## Table of Contents

- Features
- Project Architecture
- Screenshots
- Project Structure
- Installation
- Environment Variables
- Build Vector Index
- Run Query
- Tech Stack
- Contributing
- License

## 🚀 Features

- Ultra-fast inference using Groq Llama 3
- RAG over YouTube transcripts, PDFs, text, JSONL
- High-performance semantic search (Typesense / FAISS)
- Clean modular architecture (src/)
- Plug-and-play embedding + vector store pipeline
- Includes notebook for debugging + experimentation

## Project Structure
```
YT-RAGSense/
│
├── data/                 
├── faiss_store/          
├── notebook/             
│   └── typesense.ipynb
│
├── src/
│   ├── loaders/            # All data loaders
│   ├── embedding/          # Embedding pipeline
│   ├── vectorstore/        # Typesense + FAISS handlers
│   ├── llm/                # Groq LLM wrapper
│   └── rag_pipeline.py     # Main RAG logic
│
├── app.py                  # Build index
├── main.py                 # Query tester
├── books.jsonl
├── requirements.txt
├── pyproject.toml
└── README.md
```
<img width="750" height="355" alt="medium_simple_rag_workflow_091648ef39" src="https://github.com/user-attachments/assets/2cb8e8c8-2dea-44fd-9c61-b07ab739912d" />



## 🛠️ Installation
### 1. Clone Repo
```
git clone https://github.com/Sathya-2006/YT-RAGSense.git
cd YT-RAGSense
```

### 2. Create Environment (Using UV — Recommended)
**Create environment**
 ```  uv venv```
**Activate**
   **Windows:** ``` .venv\Scripts\activate ```
  

### 3. Install dependencies
 ```  uv pip install -r requirements.txt ```

### 4. Environment Variables
**Create a .env file:**
```GROQ_API_KEY=your_api_key
TYPESENSE_API_KEY=your_typesense_key
TYPESENSE_HOST=ziktplh30uqsjbw6p-1.a1.typesense.net
TYPESENSE_PORT=443
TYPESENSE_PROTOCOL=https
```
### Build Vector Index
 ```
python app.py
```
**This will:**
✔ Load data
✔ Split text
✔ Generate embeddings
✔ Store vectors in Typesense / FAISS

### Run Query
```
python main.py
```


**Example usage:**
```
from src.rag_pipeline import ask_rag
print(ask_rag("What is Generative AI?"))
```
# Tech Stack
- Python 3.10+
- Typesense / FAISS
- Groq API (Llama 3.x, Mixtral)
- LangChain Community
- HuggingFace Embeddings
- UV (Virtual environment + package manager)

## 🤝 Contributing

Pull requests, issues, and suggestions are welcome!

## 📄 License

MIT License

## ⭐ Support

If you like this repo, consider giving it a star ⭐ on GitHub!
