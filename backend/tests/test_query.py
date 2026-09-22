from fastapi.testclient import TestClient

from backend.main import app


client = TestClient(app)


def test_health():
    response = client.get("/health")

    assert response.status_code == 200
    assert response.json()["status"] == "healthy"


def test_query_structure():
    response = client.post(
        "/query",
        json={
            "question": "هل اللبس ده مناسب للجامعة؟",
            "outfit_context": (
                "jacket (confidence: 0.86), "
                "pants (confidence: 0.94), "
                "shoe (confidence: 0.63)"
            ),
        },
    )

    assert response.status_code == 200

    data = response.json()

    assert "answer" in data
    assert "sources" in data
    assert isinstance(data["sources"], list)