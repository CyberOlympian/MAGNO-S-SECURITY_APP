from app.main import app


def test_health():
    with app.test_client() as client:
        response = client.get("/health")
        assert response.status_code == 200
        assert response.json == {"status": "ok"}


def test_echo():
    with app.test_client() as client:
        response = client.post("/echo", json={"message": "hello devsecops"})
        assert response.status_code == 200
        assert response.json == {"echo": "hello devsecops"}
