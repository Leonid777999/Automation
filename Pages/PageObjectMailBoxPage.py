from selenium.webdriver.common.by import By
from Pages.PageObjectBaseClass import BaseClass



class MailBox(BaseClass):

    def __init__(self, browser):
        super().__init__(browser)

    email_last = By.XPATH, "//*[@id='mesgList']/form/div[1]/a/span[3]/span"
    email_before_the_last = By.XPATH, "//*[@id='mesgList']/form/div[2]/a/span[3]/span"

    def get_email_title(self,email):
        return self.browser.find_element(*email)

