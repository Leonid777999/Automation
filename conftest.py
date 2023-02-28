import pytest
from selenium import webdriver

@pytest.fixture
def init_browser():
    url = "https://i.ua"
    browser = webdriver.Chrome()
    browser.get(url)
    yield browser
    browser.quit()