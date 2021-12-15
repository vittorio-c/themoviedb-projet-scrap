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


def test_it_can_paginate_with_correct_page_size(movie_col):
    query_movie.movie_collection = movie_col
    movie_results = query_movie.get_movies_paginated(15, 1)

    assert len(movie_results) == 15


def test_it_can_paginate_with_correct_page_size_and_correct_page_number(movie_col):
    query_movie.movie_collection = movie_col
    first_page = query_movie.get_movies_paginated(15, 1)
    second_page = query_movie.get_movies_paginated(15, 2)

    # Use set operations to assert that no movies
    # of first page are in second page. If true,
    # this means pagination is successfull.
    first = {movie["_id"] for movie in first_page}
    second = {movie["_id"] for movie in second_page}
    assert len(first & second) == 0
    assert len(second_page) == 15


@pytest.mark.parametrize(
    "sort, order, reverse",
    [
        ("release_year", "1", False),
        ("release_year", "-1", True),
        ("title", "1", False),
        ("title", "-1", True),
        ("user_rating", "1", False),
        ("user_rating", "-1", True),
        ("budget", "1", False),
        ("budget", "-1", True),
    ],
)
def test_it_can_paginate_and_sort(movie_col, sort, order, reverse):
    query_movie.movie_collection = movie_col
    movie_results = query_movie.get_movies_paginated(15, 1, sort, order)
    ordered_years = [movie[sort] for movie in movie_results]

    assert sorted(ordered_years, reverse=reverse) == ordered_years
