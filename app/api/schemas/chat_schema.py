from pydantic import BaseModel, Field


class ChatRequest(BaseModel):
    question: str = Field(
        ...,
        min_length=1,
        description="Question sent by the user."
    )


class ChatResponse(BaseModel):
    answer: str