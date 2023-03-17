from __future__ import annotations

from selenium.webdriver.chrome import webdriver
from pages.po_base_class import BaseClass
from pages.po_send_status_page import SendStatus
from constants.locators.new_email import NewEmailLocators


class NewEmail(BaseClass):

    def __init__(self, browser: webdriver):
        super().__init__(browser)

    def fill_the_receiver_field(self, receiver: str) -> NewEmail:
        return self.fill_the_field(NewEmailLocators.FIELD_TO, receiver)

    def fill_the_subject_field(self, subject: str) -> NewEmail:
        return self.fill_the_field(NewEmailLocators.FIELD_SUBJECT, subject)

    def fill_the_text_field(self, text: str) -> NewEmail:
        return self.fill_the_field(NewEmailLocators.FIELD_TEXT, text)

    def click_send_mail_button(self) -> NewEmail:
        return self.click_button(NewEmailLocators.SEND_MAIL_BUTTON)

    def create_new_mail(self, receiver: str, subject: str, text: str) -> SendStatus:
        self.fill_the_receiver_field(receiver)
        self.fill_the_subject_field(subject)
        self.fill_the_text_field(text)
        self.click_send_mail_button()
        return SendStatus(self.browser)
