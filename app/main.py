from fastapi import FastAPI

app = FastAPI(
    title = "DocuMind AI",
    description = "agente de IA para documentos PDF realizado con Gemini",
    version = "1.0.0"
)

@app.get("/")
def root(): 
    return {
        "message" : "Welcom to DocuMind AI"
    }

@app.get("/health")
def health():
    return {
        "status" : "UP"
    }