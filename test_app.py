import pytest

from app import app as flask_app

@pytest.fixture
def app():
    yield flask_app


@pytest.fixture
def client(app):
    return app.test_client()


def test_hello_world(client):
    res = client.get('/')
    assert res.status_code == 200
    assert res.data == b'Hello, World!'

def test_multiply(client):
    res = client.get('/multiply/6/7')
    assert res.status_code == 200
    assert res.data == b'The result is 42'
