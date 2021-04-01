from flask import Flask
from datetime import datetime
from flask import Flask, render_template, request
import queries.movies as query_movie
import queries.artists as query_artist

app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello, World!"

@app.route("/movies/")
def movies():
    movies = query_movie.get_movies_with_artists()
    return render_template("movies.html", movies=movies)
