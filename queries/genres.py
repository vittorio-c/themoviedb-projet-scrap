import pandas as pd
from connection.client import client
from queries.sorts import get_aggregate_sorts
from utilities.plot import plot

movie_collection = client.themoviedb.movies_tests

# def get_genres():
