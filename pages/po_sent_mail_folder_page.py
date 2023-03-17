from __future__ import annotations
from selenium.webdriver.chrome import webdriver
from constants.locators.sent_mail_folder_page import SentMailFolderLocators
from pages.po_base_class import BaseClass


class SentMailFolder(BaseClass):

    def __init__(self, browser: webdriver):
        super().__init__(browser)

    def get_title_of_sent_mail(self) -> SentMailFolder:
        return self.get_text(SentMailFolderLocators.SENT_MAIL)
