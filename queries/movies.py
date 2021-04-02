from connection.client import client
from queries.filters import get_aggregate_filters
from queries.sorts import get_aggregate_sorts

movie_collection = client.themoviedb.movies_tests

def get_movie(id):
    movie = movie_collection.find({'_id': id})
    return movie[0]

def get_movies_paginated(page_size, page_num, sorts = {}, order = 1):
    skips = page_size * (page_num - 1)

    limit = { "$limit": page_size }
    skip = { "$skip": skips }

    if len(sorts) > 0:
        agg_sorts = get_aggregate_sorts(sorts, order)
        aggregate = [agg_sorts, skip, limit]
    else:
        # we default sorts to release_year and desc order
        agg_sorts = { "$sort" : { "release_year" : int(order) }}
        aggregate = [agg_sorts, skip, limit]

    cursor = movie_collection.aggregate(aggregate)

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


