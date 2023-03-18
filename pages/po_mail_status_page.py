from __future__ import annotations
from selenium import webdriver
from constants.locators.sent_mail_folder_page import SentMailFolderLocators
from pages.po_base_class import BaseClass
from constants.locators.mail_status_page import MailStatusLocators
from pages.sent_mail_folder import SentMailFolder


class MailStatus(BaseClass):

    def __init__(self, browser: webdriver.Chrome):
        super().__init__(browser)
        self.__browser = browser

    def open_sent_mails_folder(self) -> SentMailFolder:
        self.click_button(MailStatusLocators.SENT_MAILS_FOLDER_BUTTON)
        return SentMailFolder(self.__browser)


