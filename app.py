from src.data_loader import load_all_documents
''''from src.embedding import EmbeddingPipeline'''
from src.vectorstore import FaissVectorStore
from src.search import RAGSearch

#Example usage
if __name__ =="__main__":
    docs=load_all_documents("data")
    store=FaissVectorStore("faiss_store")
    #store.build_from_documents(docs)
    store.load()
    #print(store.query("What is attention and self attention ?",top_k=3))
    rag_search= RAGSearch()
    query="what is attention and self attention ?"
    summary= rag_search.search_and_summarize(query,top_k=3)
    print(f"Summary for query: {query}\n{summary}")



    '''chunks= EmbeddingPipeline().chunk_documents(docs)
    chunkvectors= EmbeddingPipeline().embed_chunks(chunks)

    print(chunkvectors)'''

