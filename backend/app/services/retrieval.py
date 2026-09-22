import chromadb
from sentence_transformers import SentenceTransformer

from backend.app.core.config import (
    VECTOR_STORE_PATH,
    COLLECTION_NAME,
    EMBEDDING_MODEL,
    TOP_K,
)


class RetrievalService:
    def __init__(self):
        # Load embedding model once
        self.embedding_model = SentenceTransformer(EMBEDDING_MODEL)

        # Connect to persisted ChromaDB
        self.client = chromadb.PersistentClient(
            path=str(VECTOR_STORE_PATH)
        )

        # Load existing collection
        self.collection = self.client.get_collection(
            name=COLLECTION_NAME
        )

    def retrieve(self, query: str, top_k: int = TOP_K):
        # Convert query to embedding
        query_embedding = self.embedding_model.encode(
            [query]
        )[0].tolist()

        # Search ChromaDB
        results = self.collection.query(
            query_embeddings=[query_embedding],
            n_results=top_k,
        )

        documents = results.get("documents", [[]])[0]
        ids = results.get("ids", [[]])[0]
        distances = results.get("distances", [[]])[0]

        sources = []

        for doc_id, document, distance in zip(
            ids,
            documents,
            distances
        ):
            sources.append({
                "id": doc_id,
                "content": document,
                "distance": float(distance),
            })

        return sources


retrieval_service = RetrievalService()