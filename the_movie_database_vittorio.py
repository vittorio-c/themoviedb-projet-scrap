import time
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
import pandas as pd
from bs4 import BeautifulSoup
import re
import numpy as np
import matplotlib
import sys

def accept_coockies(browser):
    cookie_button= browser.find_element_by_css_selector('#cookie_notice p:nth-child(2) a')
    if cookie_button:
        cookie_button.click()
    time.sleep(1)

def navigate_to_popular_movies(browser):
    dropdown_menu = browser.find_element_by_css_selector('ul.dropdown_menu a[href=\"/movie\"]').click()
    hidden_submenu = browser.find_element_by_css_selector("ul[data-role=\"popup\"] a[href=\"/movie\"]").click()
    time.sleep(1)

def navigate_to_infinite_scroll(browser):
    accept_coockies(browser)
    pagination_button = browser.find_element_by_css_selector('#pagination_page_1 a').click()

    SCROLL_PAUSE_TIME = 0.5
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

def get_movie_titles(soup):
    # return list avec les titles dans l'odre
    sub_soup = soup.select('div.card.style_1 div.content h2 a')
    return [movie.attrs['title'] for movie in sub_soup]

def get_movie_dates(soup):
    # return list avec les dates dans l'odre
    sub_soup = soup.select('div.card.style_1 div.content p')
    return [movie.string for movie in sub_soup]

def get_movie_rating(soup):
    # return list avec les rating dans l'odre
    sub_soup = soup.select('div.card.style_1 div.content div.consensus.tight div.user_score_chart')
    return [movie.attrs['data-percent'] for movie in sub_soup]

def get_movie_links(soup):
    # return list avec les links dans l'odre
    sub_soup = soup.select('div.card.style_1 div.content h2 a')
    return [the_moviedb_base_url + movie.attrs['href'] for movie in sub_soup]

def get_movie_genres(soup):
    sub_soup = soup.select('span.genres a')
    return [genre.string for genre in sub_soup]

def navigate_to_link(browser,link):
    browser.get(link)
    time.sleep(1)

def get_movie_budget(soup):
    budget = soup.select('section.facts.left_column p:nth-child(4)')
    print(budget)
    return budget

browser = webdriver.Firefox(executable_path=r'/home/armymen/.local/bin/geckodriver')

# =========================================
navigate_to_link(browser, 'https://www.themoviedb.org/movie/602269-little-things')
html = browser.page_source
soup = BeautifulSoup(html, 'html.parser')
budget = get_movie_budget(soup)
print(budget)

sys.exit(0)
# =========================================

the_moviedb_base_url = 'https://www.themoviedb.org/'

browser.get(the_moviedb_base_url)

accept_coockies(browser)
navigate_to_popular_movies(browser)
navigate_to_infinite_scroll(browser)

html = browser.page_source
soup = BeautifulSoup(html, 'html.parser')

titles = get_movie_titles(soup)
dates = get_movie_dates(soup)
ratings = get_movie_rating(soup)
links = get_movie_links(soup)
genres = []
budgets = []
revenues = []

for link in links:
    navigate_to_link(browser, link)
    html = browser.page_source
    soup = BeautifulSoup(html, 'html.parser')
    genres.append(get_movie_genres(soup))
    budgets.append(get_movie_budget())
    # revenues.append(get_movie_revenus())

df = pd.DataFrame(
        {
            "titles" : titles,
            "dates" : dates,
            "ratings" : ratings,
            "link" : links,
            "genres": genres
        }
        )

print(df.to_string())
