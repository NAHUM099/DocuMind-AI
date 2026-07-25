from fastapi import APIRouter, File, HTTPException, UploadFile

from app.api.schemas.upload_schema import UploadResponse
from app.services.pdf_service import PDFService

from app.services.embedding_service import EmbeddingService
from app.services.vector_store_service import VectorStoreService
from pathlib import Path

router = APIRouter(
    prefix="/api/v1",
    tags=["Upload"]
)

pdf_service = PDFService()
embedding_service = EmbeddingService()
vector_store_service = VectorStoreService()


@router.post(
    "/upload",
    response_model=UploadResponse
)
def upload_pdf(file: UploadFile = File(...)):

    if file.content_type != "application/pdf":
        raise HTTPException(
            status_code=400,
            detail="Only PDF files are allowed."
        )

    file_path = pdf_service.save_pdf(file)

    text, pages = pdf_service.extract_text(file_path)
    chunks = pdf_service.split_text(text)

    vector_store_service.save(
    chunks=chunks,
    embeddings=embedding_service.get_embeddings()
)
    Path(file_path).unlink()

    return UploadResponse(
    filename=file.filename,
    pages=pages,
    characters=len(text),
    chunks=len(chunks),
    status="processed"
    )   