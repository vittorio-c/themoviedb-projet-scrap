from connection.client import client

# Here goes all the queries for fetching artists from DB


def get_artists():
    return client.metflix.artists.find()
