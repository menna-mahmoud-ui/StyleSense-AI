from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from backend.app.api.routes.query import router as query_router


app = FastAPI(
    title="StyleSense AI",
    description="AI-powered fashion recommendation system using YOLO, RAG, and OpenAI",
    version="1.0.0",
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/health")
def health_check():
    return {
        "status": "healthy",
        "service": "StyleSense AI",
    }


app.include_router(query_router)