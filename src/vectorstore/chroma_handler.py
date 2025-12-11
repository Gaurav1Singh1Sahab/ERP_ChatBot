import chromadb
from chromadb.config import Settings

class ChromaClient:
    def __init__(self, persist_dir: str, collection_name: str):
        self.client = chromadb.Client(Settings(chroma_db_impl="duckdb+parquet",
                                                persist_directory=persist_dir))
        self.collection = self.client.get_or_create_collection(collection_name)

    def add_documents(self, docs, metadatas, ids, embeddings):
        self.collection.add(documents=docs,
                            metadatas=metadatas,
                            ids=ids,
                            embeddings=embeddings)
        self.client.persist()

    def retrieve(self, query_embedding, top_k: int):
        results = self.collection.query(query_embeddings=[query_embedding], n=top_k)
        return results
