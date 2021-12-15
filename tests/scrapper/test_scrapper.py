import time

import pytest
from dotenv import dotenv_values
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


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
    def test_accept_cookies(self):
        the_moviedb_base_url = "https://www.themoviedb.org/"
        self.driver.get(the_moviedb_base_url)
        print(self.driver.page_source)
        try:
            WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.ID, 'cookie_notice')))
            cookie_button = self.driver.find_element(
                By.CSS_SELECTOR, "#cookie_notice p:nth-child(2) a"
            )
            assert 1
        except:
            assert False
