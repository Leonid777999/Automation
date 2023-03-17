from __future__ import annotations
from selenium.webdriver.chrome import webdriver
from pages.po_base_class import BaseClass
from constants.locators.mail_status import MailStatusLocators
from constants.locators.folders_with_sent import SentMailFolderLocators


class SendStatus(BaseClass):

    def __init__(self, browser: webdriver):
        super().__init__(browser)

    def open_sent_mails_folder(self) -> SendStatus:
        return self.click_button(MailStatusLocators.SENT_MAILS_FOLDER_BUTTON)

    def get_title_of_sent_mail(self) -> SendStatus:
        return self.get_text(SentMailFolderLocators.SENT_MAIL)
