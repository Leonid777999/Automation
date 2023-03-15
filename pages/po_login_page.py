from pages.po_base_class import BaseClass
from pages.po_mailbox_page import MailBox
from locators.locators import Locators


class LoginPage(BaseClass):

    def __init__(self, browser):
        super().__init__(browser)

    def enter_login(self, login: str):
        self.fill_the_field(Locators.USER_LOGIN, login)
        return self

    def enter_passwd(self, passwd: str):
        self.fill_the_field(Locators.USER_PASSWORD, passwd)
        return self

    def click_enter_button(self):
        self.click_button(Locators.ENTER_BUTTON)
        return self

    def sign_in(self, login: str, passwd: str) -> MailBox:
        self.enter_login(login)
        self.enter_passwd(passwd)
        self.click_enter_button()
        return MailBox(self.browser)
