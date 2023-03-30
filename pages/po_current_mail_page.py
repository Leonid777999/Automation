from __future__ import annotations
from selenium import webdriver
from pages.po_base_class import BaseClass
from pages.po_new_email_page import NewEmail
from constants.locators.current_mail_page import CurrentMailLocators


class CurrentEmail(BaseClass):

    def __init__(self, browser: webdriver.Chrome):
        super().__init__(browser)
        self.__browser = browser

    def get_email_subject(self) -> str:
        return self.get_text(CurrentMailLocators.EMAIL_SUBJECT)

    def get_email_sender(self) -> str:
        return self.get_text(CurrentMailLocators.EMAIL_SENDER)

    def get_email_receiver(self) -> str:
        return self.get_text(CurrentMailLocators.EMAIL_RECEIVER)

    def goto_create_new_mail(self) -> NewEmail:
        self.click(CurrentMailLocators.CREATE_NEW_MAIL_BUTTON)
        return NewEmail(self.__browser)
