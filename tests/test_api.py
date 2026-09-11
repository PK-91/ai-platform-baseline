from fastapi.testclient import TestClient

from app.main import app


client = TestClient(app)


def test_health():
    response = client.get("/health")

    assert response.status_code == 200
    assert response.json() == {"status": "healthy"}


def test_predict_positive():
    response = client.post(
        "/predict",
        json={"text": "I love this product"}
    )

    assert response.status_code == 200

    data = response.json()

    assert data["prediction"] == "positive"