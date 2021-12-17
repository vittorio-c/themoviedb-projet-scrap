import pytest


def test_api_movies(http_client):
    response = http_client.get("/api/movies")

    assert response.status_code == 200
