from COURSE.MODULE5.main import app
from fastapi.testclient import TestClient

client = TestClient(app)


def test_read_root():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"Hello": "World"}

def test_read_db_info():
    response = client.get("/db")
    assert response.status_code == 200
    assert "connect=True" in response.json()['db']

def test_read_count_contacts():
    response = client.get("/count-contacts")
    assert response.status_code == 200
    assert isinstance(response.json()['n_contacts'], int )

# def test_read_all_contacts():
#     response = client.get("/all-contacts")
#     assert response.status_code == 200
#     assert isinstance(response.json()['all_contacts'], (list, dict) )
    