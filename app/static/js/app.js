document.getElementById("question").addEventListener("keydown", function(event) {

    if (event.key === "Enter" && !event.shiftKey) {

        event.preventDefault();

        askQuestion();

    }

});

const chat = document.getElementById("chat");
const fileInfo = document.getElementById("fileInfo");

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

    uploadButton.disabled = true;
    uploadButton.textContent = "Uploading...";

    const response = await fetch("/api/upload", {
        method: "POST",
        body: formData
    });

    const data = await response.json();

    fileInfo.textContent =
    `Loaded: ${data.filename} | Pages: ${data.pages} | Chunks: ${data.chunks}`;


    uploadButton.disabled = false;
    uploadButton.textContent = "Upload PDF";
}

async function askQuestion() {

    const question = document.getElementById("question").value;

    if (!question.trim()) {
        return;
    }

    askButton.disabled = true;

    try {

        chat.innerHTML += `
        <div class="message user">
            <strong>You</strong><br><br>
            ${question}
        </div>
        `;

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

        chat.innerHTML += `
        <div class="message ai">
            <strong>DocuMind AI</strong><br><br>
            ${data.answer}
        </div>
        `;

        chat.scrollTop = chat.scrollHeight;

        document.getElementById("question").value = "";

    } catch (error) {

        chat.innerHTML += `
        <div class="message ai">
            <strong>DocuMind AI</strong><br><br>
            Error communicating with the server.
        </div>
        `;

    } finally {

        askButton.disabled = false;

    }

}