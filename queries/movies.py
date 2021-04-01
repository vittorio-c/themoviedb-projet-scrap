from connection.client import client

# Here goes all the queries for fetching movies from DB

def get_movies():
    movies = client.metflix.movies.find()
    return movies

def get_movies_with_artists():
    movies = client.metflix.movies
    aggregate = [
        {
            "$lookup": {
                "from": "artists",
                'localField' : 'director._id',
                'foreignField' : '_id',
                'as' : 'director_qry'
                },
            },
        {
            "$lookup" :{
                "from": "artists",
                'localField' : 'actors._id',
                'foreignField' : '_id',
                'as' : 'actors_qry'
                }
            }
        ]

    movies = movies.aggregate(aggregate)
    return movies

