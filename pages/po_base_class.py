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

    def get_texts(self, position) :
        return self.wait.until(EC.presence_of_all_elements_located(position))

    def click_button(self, button) -> BaseClass:
        return self.wait.until(EC.presence_of_element_located(button)).click()

    def fill_the_field(self, field, text: str) -> BaseClass:
        return self.wait.until(EC.presence_of_element_located(field)).send_keys(text)





