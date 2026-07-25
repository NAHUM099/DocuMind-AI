from app.services.embedding_service import EmbeddingService
from app.services.gemini_service import GeminiService
from app.services.vector_store_service import VectorStoreService

from pathlib import Path
from app.config.settings import settings


class RAGService:

    def __init__(self):
        self.embedding_service = EmbeddingService()
        self.vector_store = VectorStoreService()
        self.gemini = GeminiService()

    def ask(self, question: str) -> str:
        
        vector_store_path = Path(settings.VECTOR_STORE_PATH)

        if not (vector_store_path / "index.faiss").exists():
            return (
                "No document has been uploaded yet. "
                "Please upload a PDF before asking questions."
            )

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
            Eres DocuMind AI, un asistente inteligente de análisis de documentos.

            Tu rol:
            - Responde preguntas únicamente basándote en el contexto del documento proporcionado.
            - Nunca des información si no esta relaciona con el documento.
            - Si la información falta, indica claramente que el documento no contiene la respuesta.
            - Proporciona respuestas concisas pero completas.
            - Usa un tono profesional.
            - Cuando sea posible, menciona la sección o concepto donde se encontró la respuesta.
        

            Contexto del documento:

            {context}

            Pregunta del usuario:

            {question}

            Respuesta:
            """

        return self.gemini.ask(prompt)