from selenium.webdriver.common.by import By
from Pages.PageObjectBaseClass import BaseClass



class MailBox(BaseClass):

    def __init__(self, browser):
        super().__init__(browser)

    email_last = By.XPATH, "//*[@id='mesgList']/form/div[1]/a/span[3]/span"
    email_before_the_last = By.XPATH, "//*[@id='mesgList']/form/div[2]/a/span[3]/span"

    def get_email_title(self,email):
        return self.browser.find_element(*email)
    def open_email(self, email):
        return self. browser.find_element(*email).click


class CurrentEmail(BaseClass):

    email_subject = "//div[@class='message_header iua_support clear']//child::h3"
    email_sender = "//a[@class='black']"
    email_reciever = "//div[@class='to']//child::div[2]"
    def __init__(self,browser):
        super().__init__(browser)

    def get_email_data(self, data):
        return self.browser.find_element(*data)


