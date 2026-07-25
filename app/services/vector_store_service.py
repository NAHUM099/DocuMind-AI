from pathlib import Path

from langchain_community.vectorstores import FAISS
from app.config.settings import settings


class VectorStoreService:

    def save(self, chunks: list[str], embeddings) -> None:

        vector_store = FAISS.from_texts(
            texts=chunks,
            embedding=embeddings
        )

        path = Path(settings.VECTOR_STORE_PATH)

        path.mkdir(parents=True, exist_ok=True)

        vector_store.save_local(str(path))

    def load(self, embeddings):

        path = Path(settings.VECTOR_STORE_PATH)

        return FAISS.load_local(
            str(path),
            embeddings,
            allow_dangerous_deserialization=True
        )