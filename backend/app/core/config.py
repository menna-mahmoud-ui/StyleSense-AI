from pathlib import Path
import os

from dotenv import load_dotenv

load_dotenv()

# Project root: StyleSense-AI/
BASE_DIR = Path(__file__).resolve().parents[3]

VECTOR_STORE_PATH = Path(
    os.getenv(
        "VECTOR_STORE_PATH",
        BASE_DIR / "backend" / "data" / "vector_store"
    )
)

EMBEDDING_MODEL = os.getenv(
    "EMBEDDING_MODEL",
    "sentence-transformers/all-MiniLM-L6-v2"
)

COLLECTION_NAME = os.getenv(
    "COLLECTION_NAME",
    "fashion_knowledge"
)

TOP_K = int(os.getenv("TOP_K", "3"))

OPENAI_MODEL = os.getenv(
    "OPENAI_MODEL",
    "gpt-4o-mini"
)

YOLO_MODEL = os.getenv(
    "YOLO_MODEL",
    str(BASE_DIR / "Models" / "best.pt")
)

IMAGE_SIZE = int(os.getenv("IMAGE_SIZE", "640"))

CONFIDENCE_THRESHOLD = float(
    os.getenv("CONFIDENCE_THRESHOLD", "0.25")
)