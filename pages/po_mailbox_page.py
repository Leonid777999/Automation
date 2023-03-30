from __future__ import annotations
from typing import Generator

from selenium import webdriver
from pages.po_base_class import BaseClass
from constants.locators.mailbox_page import MailBoxLocators
from pages.po_current_mail_page import CurrentEmail


class MailBox(BaseClass):

    def __init__(self, browser: webdriver.Chrome):
        super().__init__(browser)
        self.__browser = browser

    def get_first_mail_title(self) -> str:
        return self.get_text(MailBoxLocators.EMAIL_FIRST)

    def get_second_mail_title(self) -> str:
        return self.get_text(MailBoxLocators.EMAIL_SECOND)

    def get_titles(self) -> Generator:
        return (element.text for element in self.find_elements(MailBoxLocators.MESSAGE_LIST))

    #def open_email(self) -> CurrentEmail:
    #    self.click_button(MailBoxLocators.EMAIL_ROW_TO_OPEN)
    #   return CurrentEmail(self.__browser)

    def open_mail(self, title) -> CurrentEmail:
        elements = {element.text: element for element in self.find_elements(MailBoxLocators.MESSAGE_LIST)}
        return elements[title].click()

    #def get_titles_secondvariant(self):
    #   return self.get_text(element): for element in self.find_elements(MailBoxLocators.MESSAGE_LIST)

