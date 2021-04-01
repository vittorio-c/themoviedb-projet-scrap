def get_aggregate_filters(filters, order):
    if 'budget' in filters:
        aggregate = { "$sort" : { "budget" : int(order) }}
    else:
        aggregate = {}

    return aggregate

