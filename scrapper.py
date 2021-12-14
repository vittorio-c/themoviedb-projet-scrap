import json
import re
import sys
import time

import matplotlib
import numpy as np
import pandas as pd
from bs4 import BeautifulSoup
from dotenv import dotenv_values
from queries.movies import insert_or_update_movie
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys



def accept_coockies(browser):
    try:
        cookie_button = browser.find_element_by_css_selector(
            "#cookie_notice p:nth-child(2) a"
        )
        if cookie_button:
            cookie_button.click()
    except NoSuchElementException:
        pass
    time.sleep(1)


def navigate_to_popular_movies(browser):
    dropdown_menu = browser.find_element_by_css_selector(
        'ul.dropdown_menu a[href="/movie"]'
    ).click()
    hidden_submenu = browser.find_element_by_css_selector(
        'ul[data-role="popup"] a[href="/movie"]'
    ).click()
    time.sleep(1)


def navigate_to_infinite_scroll(browser):
    accept_coockies(browser)
    pagination_button = browser.find_element_by_css_selector(
        "#pagination_page_1 a"
    ).click()

    SCROLL_PAUSE_TIME = 1
    # Get scroll height
    last_height = browser.execute_script("return document.body.scrollHeight")
    count = 1
    while True:
        # Scroll down to bottom
        browser.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        # Wait to load page
        time.sleep(SCROLL_PAUSE_TIME)
        # Calculate new scroll height and compare with last scroll height
        new_height = browser.execute_script("return document.body.scrollHeight")
        if new_height == last_height or count == 1:
            break
        last_height = new_height
        count += 1


def navigate_to_link(browser, link):
    browser.get(link)
    time.sleep(1)


def get_movie_titles(soup):
    sub_soup = soup.select("section.header.poster div.title h2 a")
    return sub_soup[0].get_text("", strip=True) if len(sub_soup) else ""


def get_movie_dates(soup):
    sub_soup = soup.select("section.header.poster div.title h2 span.release_date")
    if len(sub_soup):
        date = sub_soup[0].get_text("", strip=True)
        date = date.replace("(", "")
        date = date.replace(")", "")
    else:
        date = "null"
    return int(date)


def get_movie_rating(soup):
    sub_soup = soup.select(
        "section.header.poster div.consensus.details div.user_score_chart"
    )
    return sub_soup[0].attrs["data-percent"] if len(sub_soup) else ""


def get_movie_links(soup):
    sub_soup = soup.select("div.card.style_1 div.content h2 a")
    return [the_moviedb_base_url + movie.attrs["href"] for movie in sub_soup][:key]


def get_movie_genres(soup):
    sub_soup = soup.select("section.header.poster div.title div.facts span.genres")
    if len(sub_soup):
        genre = sub_soup[0].get_text("", strip=True)
        genre = genre.split(",")
    else:
        genre = ""
    return genre


def get_movie_budget(soup):
    sub_soup = soup.select("section.facts.left_column p")

    dico = {"Budget": 0, "Recette": 0}
    if len(sub_soup):
        value_budget = [0]
        value_recette = [0]
        for element in sub_soup:
            element = element.get_text("", strip=True)
            element = element.replace(",", "")
            budget = re.findall("Budget\$(\d+)", element)
            recette = re.findall("Recette\$(\d+)", element)
            if len(budget) > 0:
                value_budget = budget

            if len(recette) > 0:
                value_recette = recette

    dico["Budget"] = int(value_budget[0])
    dico["Recette"] = int(value_recette[0])
    return dico


def get_movie_director(soup):
    sub_soup = soup.select(
        "#original_header div.header_poster_wrapper section div.header_info ol > li p:nth-child(1) a"
    )
    return sub_soup[0].get_text("", strip=True) if len(sub_soup) else ""


def get_movie_tags(soup):
    sub_soup = soup.select("div.media section.keywords ul li a")
    tags = []
    if len(sub_soup):
        for valeur in sub_soup:
            tag = valeur.get_text("", strip=True)
            tags.append(tag)
    return tags


def get_movie_picture_url(soup):
    sub_soup = soup.select(
        "#original_header div.poster_wrapper div > div.image_content.backdrop img"
    )
    return the_moviedb_base_url + sub_soup[0].attrs["src"] if len(sub_soup) else ""


def get_movie_duration(soup):
    sub_soup = soup.select(
        "#original_header div.header_poster_wrapper section div.title div span.runtime"
    )
    return sub_soup[0].get_text("", strip=True) if len(sub_soup) else ""


def calc_profit(recette_budget):

    return recette_budget["Recette"] - recette_budget["Budget"]


config = dict(dotenv_values(".env"))

browser = webdriver.Chrome(
    "./drivers/chromedriver-" + config["CHROMEDRIVER_VERSION"] + ".exe"
)
the_moviedb_base_url = "https://www.themoviedb.org/"

key = 25

browser.get(the_moviedb_base_url)

accept_coockies(browser)
navigate_to_popular_movies(browser)
navigate_to_infinite_scroll(browser)

html = browser.page_source
soup = BeautifulSoup(html, "html.parser")

links = get_movie_links(soup)

for link in links:
    navigate_to_link(browser, link)
    html = browser.page_source
    soup = BeautifulSoup(html, "html.parser")

    title = get_movie_titles(soup)
    url = link
    release_year = get_movie_dates(soup)
    user_rating = get_movie_rating(soup)
    genres = get_movie_genres(soup)
    recette_budget = get_movie_budget(soup)
    budget = recette_budget["Budget"]
    revenues = recette_budget["Recette"]
    tags = get_movie_tags(soup)
    picture_url = get_movie_picture_url(soup)
    director = get_movie_director(soup)
    duration = get_movie_duration(soup)
    profit = calc_profit(recette_budget)
    country_releases = ""
    artists = ""

    movie_tab = {
        "_id": link,
        "title": title,
        "url": link,
        "release_year": release_year,
        "user_rating": user_rating,
        "picture_url": picture_url,
        "genres": genres,
        "tags": tags,
        "budget": budget,
        "revenues": revenues,
        "profit": profit,
        "duration": duration,
        "country_releases": ["DE", "FR", "ES", "GB"],
        "director": director,
        "artists": [
            {
                "_id": "https://www.themoviedb.org/person/1663195-kelly-marie-tran",
                "role": "Raya (voice)",
                "name": "Carole Sergeant",
            },
            {
                "_id": "https://www.themoviedb.org/person/1663195-kelly-marie-tran",
                "role": "Raya (voice)",
                "name": "Carole Sergeant",
            },
            {
                "_id": "https://www.themoviedb.org/person/1663195-kelly-marie-tran",
                "role": "Raya (voice)",
                "name": "Carole Sergeant",
            },
        ],
    }

    insert_or_update_movie(movie_tab)
