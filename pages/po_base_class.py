from __future__ import annotations
from selenium.webdriver.chrome import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class BaseClass:

    def __init__(self, browser: webdriver):
        self.browser = browser
        self.wait = WebDriverWait(self.browser, 20)

    def get_text(self, position) -> BaseClass:
        return self.wait.until(EC.presence_of_element_located(position)).text

    def click_button(self, button) -> BaseClass:
        return self.wait.until(EC.presence_of_element_located(button)).click()

    def fill_the_field(self, field, text: str) -> BaseClass:
        return self.wait.until(EC.presence_of_element_located(field)).send_keys(text)
