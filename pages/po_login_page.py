from __future__ import annotations
from selenium import webdriver
from pages.po_base_class import BaseClass
from pages.po_mailbox_page import MailBox
from constants.locators.login_page import LoginPageLocators


class LoginPage(BaseClass):

    def __init__(self, browser: webdriver.Chrome):
        super().__init__(browser)
        self.__browser = browser

    def enter_login(self, login: str) -> LoginPage:
        return self.fill_the_field(LoginPageLocators.USER_LOGIN, login)

    def enter_passwd(self, passwd: str) -> LoginPage:
        return self.fill_the_field(LoginPageLocators.USER_PASSWORD, passwd)

    def click_enter_button(self) -> LoginPage:
        return self.click(LoginPageLocators.ENTER_BUTTON)

    def sign_in(self, login: str, passwd: str) -> MailBox:
        self.enter_login(login)
        self.enter_passwd(passwd)
        self.click_enter_button()
        return MailBox(self.__browser)
