import pytest
from flask import Flask

app = Flask(__name__)

def test_api_movies(http_client):
    response = http_client.get("/api/movies")
    assert response.status_code == 200

def test_routing(http_client):
    for rule in app.url_map.iter_rules():
        rv = http_client.get(str(rule))
        assert b"route" == rv.data
