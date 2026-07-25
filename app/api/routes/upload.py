from fastapi import APIRouter, File, HTTPException, UploadFile

from app.api.schemas.upload_schema import UploadResponse
from app.services.pdf_service import PDFService

router = APIRouter(
    prefix="/api",
    tags=["Upload"]
)

pdf_service = PDFService()


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

    return UploadResponse(
    filename=file.filename,
    pages=pages,
    characters=len(text),
    chunks=len(chunks),
    status="processed"
    )   