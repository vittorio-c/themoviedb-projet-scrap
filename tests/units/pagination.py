import json
import os

import mongomock
import pymongo
import pytest
import queries.movies as query_movie

client = mongomock.MongoClient()


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


def test_it_can_paginate_over_results(monkeypatch, movie_col):
    query_movie.movie_collection = movie_col

    movie_results = query_movie.get_movies_paginated(5, 1)

    assert len(movie_results) == 5
    # assert movie_results[0]['title'] == movie_col.find()[0]['title']
