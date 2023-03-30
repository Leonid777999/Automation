from __future__ import annotations
from selenium import webdriver
from pages.po_base_class import BaseClass
from pages.po_mail_status_page import MailStatus
from constants.locators.new_email_page import NewEmailLocators


class NewEmail(BaseClass):

    def __init__(self, browser: webdriver.Chrome):
        super().__init__(browser)
        self.__browser = browser

    def fill_the_receiver_field(self, receiver: str) -> NewEmail:
        return self.fill_the_field(NewEmailLocators.FIELD_TO, receiver)

    def fill_the_subject_field(self, subject: str) -> NewEmail:
        return self.fill_the_field(NewEmailLocators.FIELD_SUBJECT, subject)

    def fill_the_text_field(self, text: str) -> NewEmail:
        return self.fill_the_field(NewEmailLocators.FIELD_TEXT, text)

    def click_send_mail_button(self) -> NewEmail:
        return self.click(NewEmailLocators.SEND_MAIL_BUTTON)

    def create_new_mail(self, receiver: str, subject: str, text: str) -> MailStatus:
        self.fill_the_receiver_field(receiver)
        self.fill_the_subject_field(subject)
        self.fill_the_text_field(text)
        self.click_send_mail_button()
        return MailStatus(self.__browser)
