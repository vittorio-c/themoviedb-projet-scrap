import queries.movies as query_movie


class TestMovies:
    def test_insert_or_update_movie(self):

        movie_tab = {
            "_id": "https://www.themoviedb.org//movie/581389",
            "title": "Space Sweepers",
            "url": "https://www.themoviedb.org//movie/581389",
            "release_year": 2021,
            "user_rating": "72.0",
            "picture_url": "https://www.themoviedb.org//t/p/w300_and_h450_bestv2/vq2cqGRmhEFQ2wS4D3BMcYRoUK4.jpg",
            "genres": [
                "Drame",
                "Fantastique",
                "Science-Fiction",
            ],
            "tags": [
                "android",
                "space colony",
                "space opera",
                "space adventure",
                "spaceship",
                "ecological disaster",
            ],
            "budget": 21000000,
            "revenues": 0,
            "profit": -21000000,
            "duration": "2h 16m",
            "country_releases": ["DE", "FR", "ES", "GB"],
            "director": "Jo Sung-hee",
            "artists": [
                {
                    "_id": "https://www.themoviedb.org/person/1663195-kelly-marie-tran",
                    "role": "Raya (voice)",
                    "name": "Carole Sergeant",
                },
                {
                    "_id": "https://www.themoviedb.org/person/1663195-kelly-marie-tran",
                    "role": "Raya (voice)",
                    "name": "Carole Sergeant",
                },
                {
                    "_id": "https://www.themoviedb.org/person/1663195-kelly-marie-tran",
                    "role": "Raya (voice)",
                    "name": "Carole Sergeant",
                },
            ],
        }

        result = query_movie.insert_or_update_movie(movie_tab)

        if result:
            assert True
        else:
            assert False

    def test_get_movie(self):
        id = "https://www.themoviedb.org//movie/581389"
        movie = query_movie.movie_collection.find({"_id": id})

        if movie:
            assert True
        else:
            assert False

    def test_get_movies(self):
        movies = query_movie.get_movies()

        if movies == [movie for movie in query_movie.movie_collection.find()]:
            assert True
        else:
            assert False

    def test_get_movies_stats(self):
        value = query_movie.get_movies_stats()
        if value:
            assert True
        else:
            assert False

    def test_best_films_genres(self):
        value = query_movie.best_films_genres()
        if value:
            assert True
        else:
            assert False
