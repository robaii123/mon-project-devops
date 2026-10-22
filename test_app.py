from app import app

def test_home():
    client = app.test_client()
    response = client.get("/")
    assert response.status_code == 200
    assert response.get_json()["status"] == "success"

def test_add():
    client = app.test_client()
    response = client.get("/add/5/3")
    assert response.status_code == 200
    assert response.get_json()["result"] == 8