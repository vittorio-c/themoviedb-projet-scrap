import base64
from io import BytesIO

import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
from connection.client import client
from queries.sorts import get_aggregate_sorts
from utilities.plot import plot

movie_collection = client.themoviedb.movies


def get_movie(id):
    movie = movie_collection.find({"_id": id})
    return movie[0]


def get_movies_paginated(page_size, page_num, sorts={}, order=1):
    skips = page_size * (page_num - 1)

    limit = {"$limit": page_size}
    skip = {"$skip": skips}

    if len(sorts) > 0:
        agg_sorts = get_aggregate_sorts(sorts, order)
    else:
        # we default sorts to release_year and desc order
        agg_sorts = {"$sort": {"release_year": int(order)}}

    aggregate = [agg_sorts, skip, limit]
    cursor = movie_collection.aggregate(aggregate)

    return [movie for movie in cursor]


def get_movies():
    cursor = movie_collection.find()
    return [movie for movie in cursor]


def get_movies_stats():
    cursor = movie_collection.aggregate(
        [
            {
                "$group": {
                    "_id": "$release_year",
                    "avg_budget": {"$avg": "$budget"},
                    "avg_profit": {"$avg": "$profit"},
                    "avg_revenue": {"$avg": "$revenues"},
                }
            }
        ]
    )

    movie_stats = [movie for movie in cursor]
    df = pd.DataFrame(list(movie_stats))

    plot1 = plot(
        "_id",
        "avg_budget",
        "Années",
        "Moyenne budget",
        "Moyennes des budgets par année ",
        df,
    )
    plot2 = plot(
        "_id",
        "avg_profit",
        "Années",
        "Moyenne bénéfices",
        "Moyennes des bénéfices par année",
        df,
    )
    plot3 = plot(
        "_id",
        "avg_revenue",
        "Années",
        "Moyenne revenues",
        "Moyennes des revenues par année",
        df,
    )

    return [plot1, plot2, plot3]


# TODO : checker que movie_object est bien du json
# sinon le traiter comme un dico python ou le transformer en Json
def insert_or_update_movie(movie_object):
    return movie_collection.replace_one(
        {"_id": movie_object["_id"]}, movie_object, upsert=True
    )


def best_films_genres():
    cursor = movie_collection.aggregate(
        [
            {"$group": {"_id": "$genres", "avg_revenue": {"$avg": "$revenues"}}},
            {"$sort": {"nombre_film": -1}},
        ]
    )

    df = pd.DataFrame(list([movie for movie in cursor])).head(6)

    labels = df["_id"]
    revenues = df["avg_revenue"]
    fig1, ax1 = plt.subplots()
    ax1.pie(revenues, labels=labels, autopct="%1.1f%%", startangle=90, radius=1.5)
    plt.title(
        "Les genres des films et leurs revenues",
        fontdict={"fontweight": 600, "fontsize": 16},
        y=1.2,
    )
    plt.legend(df["_id"], bbox_to_anchor=(1.3, 1.2))

    img = BytesIO()
    plt.savefig(img, format="png")
    plt.close()
    img.seek(0)

    return base64.b64encode(img.getvalue())
