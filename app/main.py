from fastapi import FastAPI
from app.api.routes.health import router as health_router
from app.api.routes.chat import router as chat_router
from app.api.routes.upload import router as upload_router


from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from fastapi import Request
from fastapi.responses import HTMLResponse

app = FastAPI(
    title="DocuMind AI",
    description="AI Agent for PDF Documents powered by Gemini",
    version="1.0.0"
)

app.mount("/static", StaticFiles(directory="app/static"), name="static")
templates = Jinja2Templates(directory="app/templates")

app.include_router(health_router)


@app.get("/", response_class=HTMLResponse)
def home(request: Request):
    return templates.TemplateResponse(
        request=request,
        name="index.html"
    )


app.include_router(upload_router)
app.include_router(health_router)
app.include_router(chat_router)