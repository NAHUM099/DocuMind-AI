from langchain_google_genai import GoogleGenerativeAIEmbeddings

from app.config.settings import settings


class EmbeddingService:

    def __init__(self) -> None:
        self.embeddings = GoogleGenerativeAIEmbeddings(
            model="models/gemini-embedding-001",
            google_api_key=settings.GOOGLE_API_KEY
        )

    def get_embeddings(self):
        return self.embeddings