from fastapi.testclient import TestClient

from app.main import app


client = TestClient(app)


def test_health_check():
    response = client.get("/health")

    assert response.status_code == 200
    assert response.json() == {"status": "healthy"}


def test_calculator_addition():
    response = client.post(
        "/api/v1/calculator",
        json={
            "operation": "addition",
            "a": 25,
            "b": 10,
        },
    )

    assert response.status_code == 200
    assert response.json()["result"] == 35


def test_calculator_division_by_zero():
    response = client.post(
        "/api/v1/calculator",
        json={
            "operation": "division",
            "a": 10,
            "b": 0,
        },
    )

    assert response.status_code == 400
    assert response.json()["detail"] == "Cannot divide by zero."


def test_invalid_request():
    response = client.post(
        "/api/v1/calculator",
        json={
            "operation": "addition",
            "a": 25,
        },
    )

    assert response.status_code == 422