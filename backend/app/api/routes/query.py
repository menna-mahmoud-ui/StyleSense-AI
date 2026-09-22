from fastapi import APIRouter, UploadFile, File, Form
import tempfile
import os

from backend.app.schemas.query import QueryRequest, QueryResponse
from backend.app.services.retrieval import retrieval_service
from backend.app.services.generation import generation_service
from backend.app.services.detection import detection_service

router = APIRouter()


@router.post("/query", response_model=QueryResponse)
def query_style_sense(request: QueryRequest):

    rag_query = request.question

    if request.outfit_context:
        rag_query = f"""
        Detected outfit:
        {request.outfit_context}

        User question:
        {request.question}
        """

    retrieved_sources = retrieval_service.retrieve(rag_query)

    answer = generation_service.generate(
        question=request.question,
        outfit_context=request.outfit_context or "No outfit detected.",
        retrieved_sources=retrieved_sources,
    )

    sources = [
        source["id"]
        for source in retrieved_sources
    ]

    return QueryResponse(
        answer=answer,
        sources=sources,
    )


@router.post("/query/image")
async def query_image(
    image: UploadFile = File(...),
    question: str = Form(...)
):

    # Save uploaded image temporarily
    suffix = os.path.splitext(image.filename)[1] or ".jpg"

    with tempfile.NamedTemporaryFile(
        delete=False,
        suffix=suffix
    ) as temp_file:

        temp_file.write(await image.read())
        image_path = temp_file.name

    try:
        # Run YOLO
        outfit_items = detection_service.detect(image_path)

        # Convert detections to text
        if outfit_items:
            outfit_context = ", ".join(
                [
                    f"{item['item']} "
                    f"(confidence: {item['confidence']})"
                    for item in outfit_items
                ]
            )
        else:
            outfit_context = "No clothing items detected."

        # Add outfit information to RAG query
        rag_query = f"""
        Detected outfit:
        {outfit_context}

        User question:
        {question}
        """

        # Retrieve relevant fashion knowledge
        retrieved_sources = retrieval_service.retrieve(
            rag_query
        )

        # Generate recommendation
        answer = generation_service.generate(
            question=question,
            outfit_context=outfit_context,
            retrieved_sources=retrieved_sources,
        )

        sources = [
            source["id"]
            for source in retrieved_sources
        ]

        return {
            "answer": answer,
            "sources": sources,
            "detected_items": outfit_items,
        }

    finally:
        # Delete temporary image
        if os.path.exists(image_path):
            os.remove(image_path)