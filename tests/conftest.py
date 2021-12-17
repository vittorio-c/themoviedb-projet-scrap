import json
import os

import mongomock
import pytest
import queries.movies as query_movie
from app import app


@pytest.fixture
def load_movie_json():
    file_path = os.getcwd() + "/tests/data/movie_collection.json"
    with open(file_path) as file:
        movie_collection = json.load(file)
        yield movie_collection


@pytest.fixture
def movie_col(load_movie_json):
    collection = mongomock.MongoClient().themoviedb.movies
    for movie in load_movie_json:
        collection.insert_one(movie)

    yield collection


@pytest.fixture
def http_client():
    app.config["TESTING"] = True

    with app.test_client() as client:
        yield client


@pytest.fixture(autouse=True)
def setup_mocked_db(movie_col):
    # Replace Prod movie collection with Mocked movie collection for all tests
    query_movie.movie_collection = movie_col
