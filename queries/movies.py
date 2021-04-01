from connection.client import client

movie_collection = client.themoviedb.movies

def get_movie(id):
    movie = movie_collection.find({'_id': id})
    return movie[0]

def get_movies_paginated(page_size, page_num):
    """
    returns a set of documents belonging to page number `page_num`
    where size of each page is `page_size`.
    """
    # Calculate number of documents to skip
    skips = page_size * (page_num - 1)
    # Skip and limit
    cursor = movie_collection.find().skip(skips).limit(page_size)
    # Return documents
    return [movie for movie in cursor]

def get_movies():
    cursor = movie_collection.find()
    return [movie for movie in cursor]

# TODO : checker que movie_object est bien du json
# sinon le traiter comme un dico python ou le transformer en Json
def insert_or_update_movie(movie_object):
    return movie_collection.replace_one({'_id': movie_object['_id']}, movie_object, upsert=True)
