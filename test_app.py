import pytest
from app import app

@pytest.fixture
def client():
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client


def test_index(client):
    resp = client.get('/')
    assert resp.status_code == 200


def test_modules_api(client):
    resp = client.get('/api/modules')
    assert resp.status_code == 200
    assert isinstance(resp.get_json(), list)


def test_lessons_api(client):
    resp = client.get('/api/lessons/short_paras')
    assert resp.status_code == 200
    assert isinstance(resp.get_json(), list)