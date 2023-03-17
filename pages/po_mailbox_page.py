from __future__ import annotations
from selenium.webdriver.chrome import webdriver
from pages.po_base_class import BaseClass
from pages.po_new_email_page import NewEmail
from constants.locators.mailbox import MailboxLocators
from constants.locators.current_mail import CurrentMailLocators


class MailBox(BaseClass):

    def __init__(self, browser: webdriver):
        super().__init__(browser)

    def get_mail_title(self,position) -> MailBox:
        return self.get_text(position)

    def open_email(self) -> CurrentEmail:
        self.click_button(MailboxLocators.EMAIL_ROW_TO_OPEN)
        return CurrentEmail(self.browser)



class CurrentEmail(BaseClass):

    def __init__(self, browser: webdriver):
        super().__init__(browser)

    def get_email_subject(self) -> CurrentEmail:
        return self.get_text(CurrentMailLocators.EMAIL_SUBJECT)
    def get_email_sender(self) -> CurrentEmail:
        return self.get_text(CurrentMailLocators.EMAIL_SENDER)

    def get_email_receiver(self) -> CurrentEmail:
        return self.get_text(CurrentMailLocators.EMAIL_RECEIVER)

    def goto_create_new_mail(self) -> NewEmail:
        self.click_button(CurrentMailLocators.CREATE_NEW_MAIL_BUTTON)
        return NewEmail(self.browser)
