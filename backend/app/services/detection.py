from pathlib import Path

from ultralytics import YOLO

from backend.app.core.config import (
    IMAGE_SIZE,
    CONFIDENCE_THRESHOLD,
)


# Project root: StyleSense-AI/
BASE_DIR = Path(__file__).resolve().parents[3]

MODEL_PATH = BASE_DIR / "Models" / "best.pt"


class DetectionService:
    def __init__(self):
        if not MODEL_PATH.exists():
            raise FileNotFoundError(
                f"YOLO model not found at: {MODEL_PATH}"
            )

        self.model = YOLO(str(MODEL_PATH))

    def detect(self, image_path: str):
        results = self.model.predict(
            source=image_path,
            imgsz=IMAGE_SIZE,
            conf=CONFIDENCE_THRESHOLD,
            verbose=False,
        )

        result = results[0]

        outfit_items = []

        for box in result.boxes:
            class_id = int(box.cls[0])
            confidence = float(box.conf[0])
            class_name = result.names[class_id]

            outfit_items.append(
                {
                    "item": class_name,
                    "confidence": round(confidence, 3),
                }
            )

        return outfit_items


detection_service = DetectionService()