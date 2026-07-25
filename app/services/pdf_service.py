from pathlib import Path
from uuid import uuid4

from fastapi import UploadFile
from pypdf import PdfReader

from app.config.settings import settings
from langchain_text_splitters import RecursiveCharacterTextSplitter


class PDFService:

    def save_pdf(self, file: UploadFile) -> Path:
        upload_dir = Path(settings.UPLOAD_FOLDER)
        upload_dir.mkdir(parents=True, exist_ok=True)

        extension = Path(file.filename).suffix

        filename = f"{uuid4()}{extension}"

        file_path = upload_dir / filename

        with open(file_path, "wb") as buffer:
            buffer.write(file.file.read())

        return file_path

    def extract_text(self, file_path: Path) -> tuple[str, int]:
        reader = PdfReader(file_path)

        text = ""

        for page in reader.pages:
            extracted = page.extract_text()
            if extracted:
                text += extracted + "\n"

        return text, len(reader.pages)

    def split_text(self, text: str) -> list[str]:

        splitter = RecursiveCharacterTextSplitter(
            chunk_size=1000,
            chunk_overlap=200
        )

        return splitter.split_text(text)