from __future__ import annotations
from selenium.webdriver.chrome import webdriver
from pages.po_base_class import BaseClass
from constants.locators.mail_status_page import MailStatusLocators
from constants.locators.sent_mail_folder_page import SentMailFolderLocators


class MailStatus(BaseClass):

    def __init__(self, browser: webdriver):
        super().__init__(browser)

    def open_sent_mails_folder(self) -> MailStatus:
        return self.click_button(MailStatusLocators.SENT_MAILS_FOLDER_BUTTON)

    def get_title_of_sent_mail(self) -> MailStatus:
        return self.get_text(SentMailFolderLocators.SENT_MAIL)
