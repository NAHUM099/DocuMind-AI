from langchain_google_genai import ChatGoogleGenerativeAI
from app.config.settings import settings


class GeminiService : 
    """
    Service encargado de la comunicacion con gemini.
    """

    def __init__(self) -> None: 
        self.llm = ChatGoogleGenerativeAI(
            model=settings.MODEL_NAME,
            google_api_key = settings.GOOGLE_API_KEY,
            temperature = 0.2
        )

    def ask(self, question: str) -> str:
        response = self.llm.invoke(question)

        if hasattr(response, "text") and response.text:
            return response.text

        if isinstance(response.content, str):
            return response.content

        if isinstance(response.content, list):
            texts = []

            for item in response.content:
                if isinstance(item, dict):
                    text = item.get("text")
                    if text:
                        texts.append(text)

            return "\n".join(texts)

        return str(response.content)