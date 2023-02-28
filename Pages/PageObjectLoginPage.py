from selenium.webdriver.common.by import By
from PageObjectBaseClass import BaseClass
class LoginPage(BaseClass):

    def __init__(self, browser):
        super().__init__(browser)

    user_login = By.XPATH,"//input[@name='login']"
    user_password = By.XPATH,"//input[@name='pass']"
    enter = By.XPATH,"//input[@tabindex='5']"


    def enter_user_login(self,login):
        self.browser.find_element(*self.user_login).send_keys(login)

    def enter_user_password(self,password):
        self.browser.find_element(*self.user_password).send_keys(password)

