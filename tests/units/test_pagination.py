import types

import pytest
import queries.movies as query_movie
from utilities.paginate import get_pagination_routes


def test_it_can_paginate_with_correct_page_size():
    movie_results = query_movie.get_movies_paginated(15, 1)

    assert len(movie_results) == 15


def test_it_can_paginate_with_correct_page_size_and_correct_page_number():
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
def test_it_can_paginate_and_sort(sort, order, reverse):
    movie_results = query_movie.get_movies_paginated(15, 1, sort, order)
    ordered_years = [movie[sort] for movie in movie_results]

    assert sorted(ordered_years, reverse=reverse) == ordered_years


def test_it_builds_correct_pagination_urls():
    request = types.SimpleNamespace(
        url="http://localhost:5000/movies?sorts[]=release_year&order=1page=2"
    )
    expected = {
        "next": "http://localhost:5000/movies?sorts[]=release_year&order=1page=3",
        "previous": "http://localhost:5000/movies?sorts[]=release_year&order=1page=1",
        "current": 2,
    }

    pagination_route = get_pagination_routes(2, request)

    assert pagination_route == expected
