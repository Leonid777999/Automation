from selenium.webdriver.common.by import By
from PageObjectBaseClass import BaseClass
class LoginPage(BaseClass):

    def __init__(self, browser):
        super().__init__(browser)

    user_login = By.XPATH,"//input[@name='login']"
    user_password = By.XPATH,"//input[@name='pass']"
    enter_button = By.XPATH,"//input[@tabindex='5']"


    def enter_user_login(self,login:str):
        self.browser.find_element(*self.user_login).send_keys(login)

    def enter_user_password(self,password:str):
        self.browser.find_element(*self.user_password).send_keys(password)

    def click_on_enter_button(self):
        self.browser.find_element(*self.enter_button).click()