import pytest
import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from app import app


@pytest.fixture
def client():
    return app.test_client()


def test_health(client):
    res = client.get('/health')
    assert res.status_code == 200


def test_home(client):
    res = client.get('/')
    assert res.status_code == 200
