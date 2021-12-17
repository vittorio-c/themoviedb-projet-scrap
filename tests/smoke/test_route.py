import pytest
from app import app


def test_home_page_returns_correct_html_fixt(http_client):
    response = http_client.get("/")
    assert response.status_code == 200
    template = app.jinja_env.get_template("home.html")
    assert template.render() == response.get_data(as_text=True)


def test_movies_page_returns_correct_html(http_client):
    response = http_client.get("movies")
    assert response.status_code == 200
    assert b"Zone hostile" in response.data
    assert b"<form" in response.data
    assert b"<input" in response.data


def test_moviesstates_page_returns_correct_html(http_client):
    response = http_client.get("movies/stats")
    assert response.status_code == 200
    assert b"Movie Stats" in response.data
