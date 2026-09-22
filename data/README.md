# StyleSense AI

StyleSense AI is an AI-powered fashion recommendation system that combines Computer Vision, Retrieval-Augmented Generation (RAG), and a Large Language Model.

## Overview

The system analyzes an uploaded outfit image, detects clothing items using YOLO, retrieves relevant fashion knowledge from a vector database, and generates a personalized fashion recommendation.

## Architecture

```text
User Image
    ↓
YOLO Object Detection
    ↓
Detected Clothing Items
    ↓
Outfit Context
    ↓
RAG Retrieval
    ↓
Fashion Knowledge Base
    ↓
Gemini LLM
    ↓
StyleSense Recommendation# StyleSense AI

StyleSense AI is an AI-powered fashion recommendation system that combines Computer Vision, Retrieval-Augmented Generation (RAG), and a Large Language Model.

## Overview

The system analyzes an uploaded outfit image, detects clothing items using YOLO, retrieves relevant fashion knowledge from a vector database, and generates a personalized fashion recommendation.

## Architecture

```text
User Image
    ↓
YOLO Object Detection
    ↓
Detected Clothing Items
    ↓
Outfit Context
    ↓
RAG Retrieval
    ↓
Fashion Knowledge Base
    ↓
Gemini LLM
    ↓
StyleSense Recommendation
Main Features
Upload an outfit image.
Detect clothing items using YOLO.
Extract detected items and confidence scores.
Retrieve relevant fashion knowledge using RAG.
Generate Arabic fashion recommendations.
Provide retrieved knowledge sources.
Support questions about:
University outfits
Interviews
Casual style
Formal style
Sporty style
Color combinations
Accessories
Outfit improvements
Technology Stack
Python
FastAPI
Streamlit
YOLO
ChromaDB
Sentence Transformers
Gemini
Pydantic
Requests
Project Structure
StyleSense-AI/
│
├── backend/
│   ├── app/
│   │   ├── api/
│   │   │   └── routes/
│   │   ├── core/
│   │   ├── schemas/
│   │   ├── services/
│   │   └── utils/
│   │
│   ├── data/
│   │   ├── vector_store/
│   │   └── ...
│   │
│   ├── tests/
│   ├── main.py
│   ├── requirements.txt
│   ├── Dockerfile
│   └── .env.example
│
├── frontend/
│   ├── app.py
│   ├── api_client.py
│   ├── requirements.txt
│   └── .env.example
│
├── Models/
│   └── best.pt
│
├── notebooks/
│   └── StyleSense_AI.ipynb
│
├── config.json
├── .env
├── .gitignore
└── README.md
YOLO Model

The system uses a YOLO model trained on a colorful fashion object detection dataset.

The model detects:

Sunglasses
Hat
Jacket
Shirt
Pants
Shorts
Skirt
Dress
Bag
Shoe

The trained model is stored locally as:

Models/best.pt
RAG Pipeline

The fashion knowledge base is divided into chunks and embedded using:

sentence-transformers/all-MiniLM-L6-v2

The embeddings are stored using ChromaDB.

The system retrieves the most relevant fashion knowledge before generating the final answer.

API
Health Check
GET /health

Example response:

{
  "status": "healthy",
  "service": "StyleSense AI"
}
Text Query
POST /query
Image Query
POST /query/image

The image endpoint accepts:

Outfit image
User fashion question

It returns:

Generated recommendation
Retrieved sources
Detected clothing items
Confidence scores
Running the Backend

From the project root:

uvicorn backend.main:app --reload

The API will be available at:

http://127.0.0.1:8000

Swagger documentation:

http://127.0.0.1:8000/docs
Running the Frontend

From the project root:

streamlit run frontend/app.py

The frontend will normally open at:

http://localhost:8501
Environment Variables

Create a .env file and keep API keys private.

Example:

BACKEND_URL=http://localhost:8000
GEMINI_API_KEY=your_api_key_here

Never commit .env to GitHub.

Evaluation

The RAG pipeline was evaluated using multiple fashion-related questions covering:

University suitability
Interview suitability
Casual classification
Jacket and pants compatibility
Outfit additions
Formal occasions
Sporty style
Accessories
Information sufficiency

The evaluation retrieves the top 3 relevant contexts for each question.

Testing

Run:

pytest

The backend tests cover:

Health endpoint
Query response structure
Future Improvements
Better clothing detection accuracy
More fashion knowledge
User-specific style preferences
Color detection
Weather-aware recommendations
Occasion-aware recommendations
Multilingual recommendations
Improved evaluation metrics