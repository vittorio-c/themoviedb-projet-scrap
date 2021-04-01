from connection.client import client
from queries.filters import get_aggregate_filters

movie_collection = client.themoviedb.movies_tests

def get_movie(id):
    movie = movie_collection.find({'_id': id})
    return movie[0]

def get_movies_paginated(page_size, page_num, filters = {}, order = 1):
    # Calculate number of documents to skip
    skips = page_size * (page_num - 1)

    limit = { "$limit": page_size }
    skip = { "$skip": skips }

    aggregate_filters = get_aggregate_filters(filters, order)

    cursor = movie_collection.aggregate([limit, skip, aggregate_filters])

    return [movie for movie in cursor]

def get_movies():
    cursor = movie_collection.find()
    return [movie for movie in cursor]

def get_avg_movies_bugdet():
    # Récupérer la moyenne des budgets par Annéé
    cursor = movie_collection.aggregate(
       [
         {
           "$group":
             {
               "_id": "$release_year",
               "avgBugget": { "$avg": "$budget" }
             }
         }
       ]
    )
    
    return [movie for movie in cursor]
# TODO : checker que movie_object est bien du json
# sinon le traiter comme un dico python ou le transformer en Json
def insert_or_update_movie(movie_object):
    return movie_collection.replace_one({'_id': movie_object['_id']}, movie_object, upsert=True)


