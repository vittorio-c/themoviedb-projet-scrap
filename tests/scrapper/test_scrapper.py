import pytest
from dotenv import dotenv_values
from selenium.common.exceptions import NoSuchElementException
from selenium import webdriver

@pytest.fixture
def instantiate_driver(request):
    config = dict(dotenv_values("../../.env"))
    print(config)
    web_driver = webdriver.Chrome('../../drivers/chromedriver-'+ config['CHROMEDRIVER_VERSION'] +'.exe')
    request.cls.driver = web_driver
    yield
    web_driver.close()

@pytest.mark.usefixtures("instantiate_driver")
class BasicTest:
    pass
class TestScrapper(BasicTest):

    def test_accept_cookies(self):
        the_moviedb_base_url = 'https://www.themoviedb.org/'
        self.driver.get(the_moviedb_base_url)
        try:
            cookie_button = self.driver.find_element_by_css_selector('#cookie_notice p:nth-child(2) a')
            assert 1
        except:
            assert False
        
        # cookie_button = self.driver.find_element(By.CSS_SELECTOR('#cookie_notice p:nth-child(2) a'))
        # print(cookie_button)