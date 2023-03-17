from __future__ import annotations
from selenium.webdriver.chrome import webdriver
from pages.po_base_class import BaseClass
from constants.locators.mailbox_page import MailBoxLocators
from pages.po_current_mail_page import CurrentEmail


class MailBox(BaseClass):

    def __init__(self, browser: webdriver):
        super().__init__(browser)

    def get_mail_title(self,position) -> MailBox:
        return self.get_text(position)

    def open_email(self) -> CurrentEmail:
        self.click_button(MailBoxLocators.EMAIL_ROW_TO_OPEN)
        return CurrentEmail(self.browser)




