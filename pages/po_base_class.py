from __future__ import annotations
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class BaseClass:

    def __init__(self, browser: webdriver.Chrome):
        self.__browser = browser
        self.wait = WebDriverWait(self.__browser, 20)

    def get_text(self, position) -> str:
        return self.wait.until(EC.presence_of_element_located(position)).text

    def click_button(self, button) -> BaseClass:
        self.wait.until(EC.presence_of_element_located(button)).click()
        return self

    def fill_the_field(self, field, text: str) -> BaseClass:
        self.wait.until(EC.presence_of_element_located(field)).send_keys(text)
        return self

    def find_elements(self, locator) -> list:
        return self.wait.until(EC.visibility_of_all_elements_located(locator))
