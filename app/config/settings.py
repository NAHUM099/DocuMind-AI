from dotenv import load_dotenv
import os

# cargar las variables del archivo .env
load_dotenv()


class Settings:
    """
    Centraliza toda la configuración de la aplicación.
    """

    GOOGLE_API_KEY = os.getenv("GOOGLE_API_KEY")
    MODEL_NAME = os.getenv("MODEL_NAME", "gemini-2.5-flash")

    UPLOAD_FOLDER = "uploads"
    VECTOR_STORE_PATH = "vectorstore"


settings = Settings()