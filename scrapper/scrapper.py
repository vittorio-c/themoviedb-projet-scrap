import time
import json
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException
import pandas as pd
from bs4 import BeautifulSoup
import re
import numpy as np
import matplotlib
import sys
from dotenv import dotenv_values
from queries.movies import insert_or_update_movie

def accept_coockies(browser):
    try:
        cookie_button= browser.find_element_by_css_selector('#cookie_notice p:nth-child(2) a')
        if cookie_button:
            cookie_button.click()
    except NoSuchElementException:
        pass
    time.sleep(1)

def navigate_to_popular_movies(browser):
    dropdown_menu = browser.find_element_by_css_selector('ul.dropdown_menu a[href=\"/movie\"]').click()
    hidden_submenu = browser.find_element_by_css_selector("ul[data-role=\"popup\"] a[href=\"/movie\"]").click()
    time.sleep(1)

def navigate_to_infinite_scroll(browser):
    accept_coockies(browser)
    pagination_button = browser.find_element_by_css_selector('#pagination_page_1 a').click()

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

def navigate_to_link(browser,link):
    browser.get(link)
    time.sleep(1)

def get_movie_titles(soup):
    sub_soup = soup.select('section.header.poster div.title h2 a')
    if len(sub_soup):
        title = sub_soup[0].get_text('', strip=True)
    else:
        title = ''
    return title

def get_movie_dates(soup):
    sub_soup = soup.select('section.header.poster div.title div.facts span.release')
    if len(sub_soup):
        date = sub_soup[0].get_text('', strip=True)
    else:
        date = ''
    return date

def get_movie_rating(soup):
    sub_soup = soup.select('section.header.poster div.consensus.details div.user_score_chart')
    if len(sub_soup):
        rating = sub_soup[0].attrs['data-percent']
    else:
        rating = ''
    return rating

def get_movie_links(soup):
    sub_soup = soup.select('div.card.style_1 div.content h2 a')
    return [the_moviedb_base_url + movie.attrs['href'] for movie in sub_soup][:key]

def get_movie_genres(soup):
    sub_soup = soup.select('section.header.poster div.title div.facts span.genres')
    if len(sub_soup):
        genre = sub_soup[0].get_text('', strip=True)
        genre = genre.split(",")
    else:
        genre = ''
    return genre

def get_movie_budget(soup):
    sub_soup = soup.select('section.facts.left_column p:nth-child(5)')
    if len(sub_soup):
        budget = sub_soup[0].get_text('', strip=True)
    else:
        budget = ''
    return budget

def get_movie_director(soup):
    sub_soup = soup.select('#original_header div.header_poster_wrapper section div.header_info ol > li p:nth-child(1) a')
    if len(sub_soup):
        director = sub_soup[0].get_text('', strip=True)
    else:
        director = ''
    return director

def get_movie_tags(soup):
    sub_soup = soup.select('div.media section.keywords ul li a')
    tags = []
    if len(sub_soup):
        for valeur in sub_soup:
            tag = valeur.get_text('', strip=True)
            tags.append(tag)
    return tags

def get_movie_picture_url(soup):
    sub_soup = soup.select('#original_header div.poster_wrapper div > div.image_content.backdrop img')
    if len(sub_soup):
        picture_url = the_moviedb_base_url + sub_soup[0].attrs['src']
    else:
        picture_url = ''
    return picture_url

def get_movie_duration(soup):
    sub_soup = soup.select('#original_header div.header_poster_wrapper section div.title div span.runtime')
    if len(sub_soup):
        duration = sub_soup[0].get_text('', strip=True)
    else:
        duration = ''
    return duration


print('hello')