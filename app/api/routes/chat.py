from fastapi import APIRouter

from app.api.schemas.chat_schema import ChatRequest, ChatResponse
from app.services.rag_service import RAGService

router = APIRouter(
    prefix="/api",
    tags=["Chat"]
)

rag_service = RAGService()


@router.post(
    "/chat",
    response_model=ChatResponse
)
def chat(request: ChatRequest) -> ChatResponse:

    answer = rag_service.ask(request.question)

    return ChatResponse(
        answer=answer
    )