# DocuMind AI

Asistente inteligente para análisis de documentos PDF utilizando Inteligencia Artificial y arquitectura **RAG (Retrieval Augmented Generation)**.

Permite cargar documentos PDF, procesar su contenido y realizar preguntas utilizando Google Gemini, generando respuestas basadas únicamente en la información encontrada dentro del documento.



## Características

-  Carga y procesamiento de archivos PDF
-  Extracción y división de texto en fragmentos
-  Generación de embeddings con Google Gemini
-  Almacenamiento vectorial con FAISS
-  Preguntas y respuestas sobre documentos
-  Aplicación dockerizada
-  Configuración mediante variables de entorno
-  Health check y manejo de errores



## Tecnologías

**Backend**
- Python 3.12
- FastAPI
- LangChain
- Uvicorn

**IA**
- Google Gemini API
- Gemini Embeddings
- RAG

**Vector Database**
- FAISS

**DevOps**
- Docker
- Docker Compose




## Flujo RAG

1. Usuario carga un PDF.
2. Se extrae el contenido.
3. El documento se divide en fragmentos.
4. Se generan embeddings.
5. Se almacenan en FAISS.
6. La pregunta busca información relevante.
7. Gemini genera la respuesta usando el contexto encontrado.



## Seguridad

Archivos excluidos del repositorio:

```
.env
.venv/
uploads/
vectorstore/
__pycache__/
```



## Próximas mejoras

- Autenticación con JWT
- Gestión de usuarios
- Múltiples documentos
- PostgreSQL para persistencia
- CI/CD
- Despliegue en Cloud


Desarrollador de software enfocado en Backend, Inteligencia Artificial y tecnologías Cloud.
