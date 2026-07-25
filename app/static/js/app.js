const uploadButton = document.getElementById("uploadButton");
const askButton = document.getElementById("askButton");

uploadButton.addEventListener("click", uploadPdf);
askButton.addEventListener("click", askQuestion);

async function uploadPdf() {

    const fileInput = document.getElementById("pdfFile");

    if (fileInput.files.length === 0) {
        alert("Seleccione un PDF.");
        return;
    }

    const formData = new FormData();
    formData.append("file", fileInput.files[0]);

    const response = await fetch("/api/upload", {
        method: "POST",
        body: formData
    });

    const data = await response.json();

    alert(
        `Documento procesado

Páginas: ${data.pages}
Chunks: ${data.chunks}`
    );
}

async function askQuestion() {

    const question = document.getElementById("question").value;

    if (!question.trim()) {
        return;
    }

    const response = await fetch("/api/chat", {
        method: "POST",
        headers: {
            "Content-Type": "application/json"
        },
        body: JSON.stringify({
            question: question
        })
    });

    const data = await response.json();

    document.getElementById("response").textContent = data.answer;
}