import pandas as pd
from io import BytesIO
import base64
import matplotlib.pyplot as plt
import seaborn as sns
from connection.client import client
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

def get_movies_stats():
    cursor = movie_collection.aggregate(
       [
         {
           "$group":
             {
               "_id": "$release_year",
               "avg_budget": { "$avg": "$budget" },
               "avg_profit": { "$avg": "$profit" },
               "avg_revenue": {"$avg": "$revenues"}
             }
         }
       ]
    )

    movie_stats = [movie for movie in cursor]
    df =  pd.DataFrame(list(movie_stats))

    plot1 = plot("_id" , "avg_budget" , "Années" , "Moyenne budget" , "Moyennes des budgets par année ", df )
    plot2 = plot("_id" , "avg_profit" , "Années" , "Moyenne bénéfices" , "Moyennes des bénéfices par année", df )
    plot3 = plot("_id" , "avg_revenue" , "Années" , "Moyenne revenues" , "Moyennes des revenues par année", df )

    return [plot1,plot2,plot3]

# TODO : checker que movie_object est bien du json
# sinon le traiter comme un dico python ou le transformer en Json
def insert_or_update_movie(movie_object):
    return movie_collection.replace_one({'_id': movie_object['_id']}, movie_object, upsert=True)

def plot(x , y , labelx , labely , titre, df ):
    img = BytesIO()

    sns.set_theme(style="whitegrid")
    fig, ax = plt.subplots(figsize = (8,5))
    plt.title(titre, fontdict={'fontweight': 600,'fontsize':13},y=1)
    plt.xticks(fontweight = 600)
    plt.yticks(fontweight = 600)
    sns.barplot(x = '_id', y = y, data = df , ax = ax)
    plt.xlabel(labelx, fontsize=13, x=0.5)
    plt.ylabel(labely, fontsize=13)

    plt.savefig(img, format='png')
    plt.close()
    img.seek(0)

    return base64.b64encode(img.getvalue())
