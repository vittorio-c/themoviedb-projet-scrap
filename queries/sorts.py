def get_aggregate_sorts(sorts, order):
    aggregate = {}

    if "budget" in sorts:
        aggregate = {"$sort": {"budget": int(order)}}
    elif "revenues" in sorts:
        aggregate = {"$sort": {"revenues": int(order)}}
    elif "profit" in sorts:
        aggregate = {"$sort": {"profit": int(order)}}
    elif "release_year" in sorts:
        aggregate = {"$sort": {"release_year": int(order)}}
    elif "title" in sorts:
        aggregate = {"$sort": {"title": int(order)}}
    elif "user_rating" in sorts:
        aggregate = {"$sort": {"user_rating": int(order)}}

    return aggregate
