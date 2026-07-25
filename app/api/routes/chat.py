from fastapi import APIRouter

from app.api.schemas.chat_schema import ChatRequest, ChatResponse
from app.services.gemini_service import GeminiService

router = APIRouter(
    prefix="/api",
    tags=["Chat"]
)

gemini_service = GeminiService()


@router.post(
    "/chat",
    response_model=ChatResponse
)
def chat(request: ChatRequest) -> ChatResponse:

    answer = gemini_service.ask(request.question)

    return ChatResponse(
        answer=answer
    )