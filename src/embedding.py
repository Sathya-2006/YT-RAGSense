from typing import List,Any
from langchain_text_splitters import RecursiveCharacterTextSplitter
from sentence_transformers import SentenceTransformer
import numpy as np
from src.data_loader import load_all_documents

class EmbeddingPipeline:
    def __init__(self, model_name: str = "all-MiniLM-L6-v2", chunk_size: int = 500, chunk_overlap: int = 50):
        self.chunk_size = chunk_size
        self.chunk_overlap = chunk_overlap
        self.model = SentenceTransformer(model_name)
        print(f'[INFO] Loaded embedding model: {model_name}')

    def chunk_documents(self, documents: List[Any]) -> List[Any]:
        splitter=RecursiveCharacterTextSplitter(
            chunk_size=self.chunk_size,
            chunk_overlap=self.chunk_overlap,
            length_function=len,
            separators=["\n\n","\n"," ","",""]
        )
        chunks= splitter.split_documents(documents)
        print(f'[INFO] Split {len(documents)} documents into {len(chunks)} chunks.')
        return chunks
    
    def embed_chunks(self, documents: List[Any]) -> List[np.ndarray]:
            chunks = self.chunk_documents(documents)
            embeddings=self.model.encode([chunk.page_content for chunk in chunks])
            print(f'[INFO] Generated embeddings for {len(embeddings)} chunks.')
            return embeddings
