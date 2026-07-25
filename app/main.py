from fastapi import FastAPI
from app.api.routes.health import router as health_router
from app.api.routes.chat import router as chat_router
from app.api.routes.upload import router as upload_router

app = FastAPI(
    title="DocuMind AI",
    description="AI Agent for PDF Documents powered by Gemini",
    version="1.0.0"
)

app.include_router(health_router)


@app.get("/")
def root():
    return {
        "message": "Welcome to DocuMind AI"
    }


app.include_router(upload_router)
app.include_router(health_router)
app.include_router(chat_router)