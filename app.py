from flask import Flask
from datetime import datetime
from flask import Flask, render_template, request
import queries.movies as query_movie
import queries.artists as query_artist

app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello, World!"

@app.route("/movies")
def movies():
    page_num = request.args.get('page') if request.args.get('page') else 1
    sorts = request.args.getlist('sorts[]')
    order = request.args.get('order') if request.args.get('order') else -1
    links = get_pagination_routes(page_num)
    movies = query_movie.get_movies_paginated(15, int(page_num), sorts, order)

    return render_template("movies.html", movies=movies, links=links)

@app.route("/movies/stats")
def movies_stats():
    plot_urls = query_movie.get_movies_stats()
    plot_urls_decoded = [plot_url.decode('utf8') for plot_url in plot_urls]

    return render_template('movies_stats.html', plot_urls=plot_urls_decoded)

def get_pagination_routes(page_num):
    next_page = int(page_num) + 1
    previous_page = int(page_num) - 1 if int(page_num) - 1 > 0 else None

    if next_page:
        next_url = request.url.replace('page={}'.format(page_num), 'page={}'.format(next_page))
    else:
        next_url = False

    if previous_page:
        previous_url = request.url.replace('page={}'.format(page_num), 'page={}'.format(previous_page))
    else:
        previous_url = False

    return {'next': next_url, 'previous': previous_url}
