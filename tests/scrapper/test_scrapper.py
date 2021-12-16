import pytest
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager


@pytest.fixture
def instantiate_driver(request):
    # Define an agent to scrap the website else we are blocked
    user_agent = "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.50 Safari/537.36"
    # Declare many options to execute the tests in github Actions
    options = webdriver.ChromeOptions()
    options.add_argument("headless")
    options.add_argument(f"user-agent={user_agent}")
    # The old method is deprecated, this method load the webdriver in browser cache
    s = Service(ChromeDriverManager().install())
    # Create the webdriver
    web_driver = webdriver.Chrome(service=s, options=options)

    request.cls.driver = web_driver
    yield
    web_driver.close()


@pytest.mark.usefixtures("instantiate_driver")
class BasicTest:
    pass


class TestScrapper(BasicTest):
    def test_navigate_to_popular_movies(self):
        the_moviedb_base_url = "https://www.themoviedb.org/"
        self.driver.get(the_moviedb_base_url)

        try:
            WebDriverWait(self.driver, 3).until(
                EC.presence_of_element_located((By.ID, "main"))
            )
            elem_menu = self.driver.find_element(
                By.CSS_SELECTOR, 'ul.dropdown_menu a[href="/movie"]'
            )
            if elem_menu:
                elem_menu.click()
                if self.driver.find_element(
                    By.CSS_SELECTOR, 'ul[data-role="popup"] a[href="/movie"]'
                ):
                    assert True
        except NoSuchElementException:
            assert False

    def test_can_scroll_infinite(self):
        the_moviedb_movie_url = "https://www.themoviedb.org/movie"
        self.driver.get(the_moviedb_movie_url)

        try:
            WebDriverWait(self.driver, 3).until(
                EC.presence_of_element_located((By.ID, "main"))
            )
            btn_to_scroll = self.driver.find_element(
                By.CSS_SELECTOR, "#pagination_page_1 a"
            )
            if btn_to_scroll:
                assert True
        except NoSuchElementException:
            assert False

    @pytest.mark.parametrize(
        "elem_selector",
        [
            ("div.card.style_1 div.content h2 a")
        ],
    )
    def test_get_title_movie_homepage(self, elem_selector):
        the_moviedb_movie_url = "https://www.themoviedb.org"
        self.driver.get(the_moviedb_movie_url)

        try:
            WebDriverWait(self.driver, 3).until(
                EC.presence_of_element_located((By.ID, "main"))
            )
            if self.driver.find_elements(By.CSS_SELECTOR, elem_selector):
                assert True
        except NoSuchElementException:
            assert False


    @pytest.mark.parametrize(
        "elem_selector",
        [
            ("section.header.poster div.title h2 a"),
            ("section.header.poster div.title h2 span.release_date"),
            ("section.header.poster div.consensus.details div.user_score_chart"),
            ("section.header.poster div.title div.facts span.genres"),
            ("section.facts.left_column p"),
            ("#original_header div.header_poster_wrapper section div.header_info ol > li p:nth-child(1) a"),
            ("div.media section.keywords ul li a"),
            ("#original_header div.poster_wrapper div > div.image_content.backdrop img"),
            ("#original_header div.header_poster_wrapper section div.title div span.runtime")
        ],
    )
    def test_get_elements_in_movie_details(self, elem_selector):
        the_moviedb_movie_url = "https://www.themoviedb.org/movie"
        self.driver.get(the_moviedb_movie_url)

        try:
            WebDriverWait(self.driver, 3).until(
                EC.presence_of_element_located((By.ID, "main"))
            )
            first_movie = self.driver.find_element(
                By.CSS_SELECTOR, "#media_results a[href*='/movie/']"
            )
            if first_movie:
                first_movie.click()
                if self.driver.find_element(By.CSS_SELECTOR, elem_selector):
                    assert True
        except NoSuchElementException:
            assert False
