````markdown
# 👗 StyleSense AI

AI-powered fashion recommendation system that combines Computer Vision, RAG, and Large Language Models to analyze outfits and provide context-aware fashion recommendations.

## 📌 Project Overview

StyleSense AI allows users to upload an outfit image and ask fashion-related questions.

The system first detects clothing items using a custom-trained YOLO model. The detected items are then converted into structured outfit context and combined with retrieved fashion knowledge from a ChromaDB vector database.

An LLM uses the detected outfit and retrieved knowledge to generate a grounded fashion recommendation.

## 🏗️ System Architecture

```text
User Image
    ↓
YOLO Object Detection
    ↓
Detected Clothing Items
    ↓
Structured Outfit Context
    ↓
RAG Retrieval
    ↓
Fashion Knowledge Base
    ↓
LLM Generation
    ↓
StyleSense AI Recommendation
````

## ✨ Features

* Upload outfit images
* Clothing item detection using YOLO
* Confidence scores for detected items
* Fashion knowledge retrieval using RAG
* ChromaDB persistent vector store
* Semantic embeddings using Sentence Transformers
* Context-aware fashion recommendations
* Arabic question answering
* Source/chunk references for retrieved knowledge
* FastAPI backend
* Streamlit frontend
* API documentation using Swagger UI

## 🧠 AI Pipeline

### 1. Computer Vision

A YOLO model was trained on the Colorful Fashion Dataset for Object Detection.

The model detects:

* Sunglasses
* Hat
* Jacket
* Shirt
* Pants
* Shorts
* Skirt
* Dress
* Bag
* Shoe

### 2. Retrieval-Augmented Generation

The fashion knowledge base contains information about:

* Casual outfits
* Formal outfits
* Sporty outfits
* Neutral colors
* Monochromatic combinations
* Complementary colors
* Color balance
* Shirt and pants combinations
* Shirt and skirt combinations
* Jackets
* Dresses
* University outfits
* Interview outfits
* Accessories
* Style recommendations

The documents are split into chunks and embedded using:

`sentence-transformers/all-MiniLM-L6-v2`

The embeddings are stored in ChromaDB.

### 3. LLM Generation

The retrieved fashion knowledge and detected outfit context are provided to the LLM to generate a grounded answer in Arabic.

## 🛠️ Tech Stack

| Component            | Technology            |
| -------------------- | --------------------- |
| Programming Language | Python                |
| Computer Vision      | YOLO / Ultralytics    |
| Embeddings           | Sentence Transformers |
| Vector Database      | ChromaDB              |
| Backend              | FastAPI               |
| Frontend             | Streamlit             |
| LLM                  | Gemini                |
| Testing              | Pytest                |
| API Documentation    | Swagger / OpenAPI     |

## 📁 Project Structure

```text
StyleSense-AI/
│
├── backend/
│   ├── app/
│   │   ├── api/
│   │   │   └── routes/
│   │   │       ├── query.py
│   │   │       └── image.py
│   │   │
│   │   ├── core/
│   │   │   └── config.py
│   │   │
│   │   ├── schemas/
│   │   │   └── query.py
│   │   │
│   │   ├── services/
│   │   │   ├── generation.py
│   │   │   ├── retrieval.py
│   │   │   └── yolo_service.py
│   │   │
│   │   └── utils/
│   │
│   ├── data/
│   │   └── vector_store/
│   │
│   ├── tests/
│   │   └── test_query.py
│   │
│   ├── .env.example
│   ├── Dockerfile
│   ├── main.py
│   └── requirements.txt
│
├── frontend/
│   ├── app.py
│   ├── api_client.py
│   ├── .env.example
│   └── requirements.txt
│
├── Models/
│   └── best.pt
│
├── notebooks/
│   └── StyleSense_AI.ipynb
│
├── config.json
├── .gitignore
└── README.md
```

## 🚀 Installation

Clone the repository:

```bash
git clone <YOUR_GITHUB_REPOSITORY_URL>
cd StyleSense-AI
```

Create a virtual environment:

```bash
python -m venv .venv
```

Activate it on Windows:

```powershell
.venv\Scripts\activate
```

Install backend dependencies:

```bash
pip install -r backend/requirements.txt
```

Install frontend dependencies:

```bash
pip install -r frontend/requirements.txt
```

## 🔐 Environment Variables

Create a `.env` file in the project root.

Do not commit the `.env` file or expose API keys publicly.

Example:

```text
GEMINI_API_KEY=your_api_key_here
BACKEND_URL=http://localhost:8000
```

## ▶️ Running the Backend

From the project root:

```bash
uvicorn backend.main:app --reload
```

The backend will run at:

```text
http://127.0.0.1:8000
```

## 📚 API Documentation

Swagger UI:

```text
http://127.0.0.1:8000/docs
```

### Health Check

```http
GET /health
```

### Text Query

```http
POST /query
```

Example:

```json
{
    "question": "هل اللبس ده مناسب للجامعة؟",
    "outfit_context": "jacket (confidence: 0.86), pants (confidence: 0.94), shoe (confidence: 0.63)"
}
```

### Image Query

```http
POST /query/image
```

The endpoint accepts an outfit image and a fashion question.

The system detects clothing items using YOLO and automatically passes the detected outfit context to the RAG and generation pipeline.

## 🖥️ Running the Frontend

From the project root:

```bash
streamlit run frontend/app.py
```

The application will open in the browser.

## 📊 Evaluation

The RAG pipeline was evaluated using 10 fashion-related questions covering:

* University suitability
* Job interview suitability
* Casual classification
* Jacket and pants compatibility
* Additional clothing recommendations
* Formal occasions
* Sporty classification
* Accessories
* Outfit compatibility
* Knowledge sufficiency

For each question, the system retrieves the top 3 relevant knowledge chunks and generates an answer based on the retrieved context.

## ⚠️ Failure Cases

The evaluation identified several possible limitations:

1. Low-confidence YOLO detections can introduce incorrect outfit context.
2. The knowledge base may not contain enough information for some questions.
3. Style categories such as "Sporty" or "Formal" can be ambiguous.
4. YOLO detects clothing categories but does not fully understand fabric, exact color shades, fit, or personal preferences.
5. Retrieval mismatch can reduce the quality of the generated recommendation.

## 🧪 Testing

Run the backend tests:

```powershell
$env:PYTHONPATH="."
pytest backend/tests/test_query.py -v
```

Current tests cover:

* Health endpoint
* Query endpoint response structure

## 🔒 Security

API keys must be stored in environment variables and must never be committed to GitHub.

The following files and directories should remain excluded from version control:

```text
.env
.venv/
__pycache__/
*.pt
vector_store/
```

## 📌 Future Improvements

* Improve YOLO detection accuracy with additional training
* Add clothing color detection
* Detect clothing attributes such as style and pattern
* Expand the fashion knowledge base
* Add user preferences
* Improve evaluation with quantitative retrieval metrics
* Add recommendation personalization
* Deploy the backend and frontend

```