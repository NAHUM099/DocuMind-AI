from app.services.embedding_service import EmbeddingService
from app.services.gemini_service import GeminiService
from app.services.vector_store_service import VectorStoreService


class RAGService:

    def __init__(self):
        self.embedding_service = EmbeddingService()
        self.vector_store = VectorStoreService()
        self.gemini = GeminiService()

    def ask(self, question: str) -> str:

        db = self.vector_store.load(
            self.embedding_service.get_embeddings()
        )

        documents = db.similarity_search(
            question,
            k=4
        )

        context = "\n\n".join(
            doc.page_content
            for doc in documents
        )

        prompt = f"""
You are an assistant that answers ONLY using the provided context.

Context:

{context}

Question:

{question}

If the answer is not present in the context, say that the information is not available in the uploaded document.
"""

        return self.gemini.ask(prompt)