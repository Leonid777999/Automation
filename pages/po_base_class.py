from __future__ import annotations

from typing import Union

from selenium import webdriver
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class BaseClass:

    def __init__(self, browser: webdriver.Chrome):
        self.__browser = browser
        self.wait = WebDriverWait(self.__browser, 20)

    def get_text(self, element: Union[tuple, WebElement]) -> str:
        if isinstance(element, tuple):
            element = self.find_element(element)
        else:
            element = self.wait.until(EC.presence_of_element_located(element))
        return element.text

    def click(self, element: Union[tuple, WebElement]) -> BaseClass:
        if isinstance(element, tuple):
            element = self.find_element(element)
        else:
            element = self.wait.until(EC.visibility_of_element_located(element))
        element.click()
        return self

    def fill_the_field(self, element: Union[tuple, WebElement], text) -> BaseClass:
        if isinstance(element, tuple):
            element = self.find_element(element)
        else:
            element = self.wait.until(EC.visibility_of_element_located(element))
        element.send_keys(text)
        return self

    def find_elements(self, element) -> list:
        return self.wait.until(EC.visibility_of_all_elements_located(element))

    def find_element(self, element) -> WebElement:
        return self.wait.until(EC.visibility_of_element_located(element))

