from connection.client import client

# Here goes all the queries for fetching artists from DB


def get_artists():
    artists = client.metflix.artists.find()
    return artists
