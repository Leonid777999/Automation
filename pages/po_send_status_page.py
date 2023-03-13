from selenium.webdriver.common.by import By
from pages.po_base_class import BaseClass
from locators.locators import Locators

class Send_status(BaseClass):

    def __init__(self, browser):
        super().__init__(browser)

    def open_sended_mails_folder(self):
        self.click_button(Locators.SENDED_MAILS_FOLDER_BUTTON)
        return self

    def get_title_of_sended_mail(self):
        get_title = self.get_text(Locators.SENDED_MAIL)
        return get_title


