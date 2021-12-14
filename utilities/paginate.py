def get_pagination_routes(page_num, request):
    next_page = int(page_num) + 1
    previous_page = int(page_num) - 1 if int(page_num) - 1 > 0 else None

    if next_page:
        next_url = request.url.replace(
            "page={}".format(page_num), "page={}".format(next_page)
        )
    else:
        next_url = False

    if previous_page:
        previous_url = request.url.replace(
            "page={}".format(page_num), "page={}".format(previous_page)
        )
    else:
        previous_url = False

    return {"next": next_url, "previous": previous_url}
