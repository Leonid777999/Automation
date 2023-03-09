from selenium.webdriver.common.by import By
from Pages.PO_Base_Class import BaseClass
class LoginPage(BaseClass):

    def __init__(self, browser):
        super().__init__(browser)

    user_login = By.XPATH,"//input[@name='login']"
    user_password = By.XPATH,"//input[@name='pass']"
    enter_button = By.XPATH,"//input[@tabindex='5']"




