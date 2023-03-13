from selenium.webdriver.common.by import By
from Pages.po_base_class import BaseClass
from Pages.po_mailbox_page import MailBox


class LoginPage(BaseClass):

    def __init__(self, browser):
        super().__init__(browser)

    user_login = By.XPATH, "//input[@name='login']"
    user_password = By.XPATH, "//input[@name='pass']"
    enter_button = By.XPATH, "//input[@tabindex='5']"

    def enter_login(self, login):
        self.fill_the_field(self.user_login, login)
        return self

    def enter_passwd(self, passwd):
        self.fill_the_field(self.user_password, passwd)
        return self

    def click_enter_button(self):
        self.click_button(self.enter_button)
        return self

    def sign_in(self, login, passwd):
        self.enter_login(login)
        self.enter_passwd(passwd)
        self.click_button(self.enter_button)
        return MailBox(self.browser)
