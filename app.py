import os
from datetime import datetime

import queries.artists as query_artist
import queries.movies as query_movie
from flask import Flask, jsonify, redirect, render_template, request
from flask.helpers import url_for
from flask_cors import CORS
from utilities.paginate import get_pagination_routes

app = Flask(__name__)

# enable CORS
CORS(app, resources={r"/*": {"origins": "*"}})


# sanity check route
@app.route("/ping", methods=["GET"])
def ping_pong():
    return jsonify("pong !")


@app.route("/")
def hello():
    return render_template("home.html")


@app.route("/moviedb")
def index():
    # Default sorting
    return redirect(url_for("movies") + "?sorts[]=release_year&order=-1&page=1")


@app.route("/movies")
def movies():
    page_num = request.args.get("page") or 1
    sorts = request.args.getlist("sorts[]")
    order = request.args.get("order") or -1
    links = get_pagination_routes(page_num, request)
    movies = query_movie.get_movies_paginated(15, int(page_num), sorts, order)

    return render_template("movies.html", movies=movies, links=links)


@app.route("/movies/stats")
def movies_stats():
    plot_urls = query_movie.get_movies_stats()
    plot_urls.append(query_movie.best_films_genres())
    plot_urls_decoded = [plot_url.decode("utf8") for plot_url in plot_urls]

    return render_template("movies_stats.html", plot_urls=plot_urls_decoded)


@app.route("/performances")
def performances():
    return render_template("performances.html")


@app.route("/report")
def reports():
    nb_users = request.args.get("nbusers")
    print(os.path.join("performance", "report_" + nb_users + "_users.html"))
    # exit()
    # return app.send_static_file(os.path.join(app.root_path, "templates","performance", "report_"+ nb_users + "_users.html"))
    return app.send_static_file("report_" + nb_users + "_users.html")


@app.route("/api/movies", methods=["GET"])
def api_movies():
    page_num = request.args.get("page") or 1
    sorts = request.args.getlist("sorts[]")
    order = request.args.get("order") or -1
    links = get_pagination_routes(page_num, request)
    movies = query_movie.get_movies_paginated(15, int(page_num), sorts, order)

    return jsonify({"data": movies, "_embed": links})
