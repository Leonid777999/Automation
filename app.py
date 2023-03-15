from selenium import webdriver
from pages.po_login_page import LoginPage
from pages.po_mailbox_page import MailBox, CurrentEmail
from pages.po_new_email_page import NewEmail
from pages.po_send_status_page import SendStatus


class App:

    URL = "https://www.i.ua/"

    def __init__(self):

        self.__browser = webdriver.Chrome()

        self.login_page = LoginPage(self.__browser)
        self.mailbox_page = MailBox(self.__browser)
        self.current_email = CurrentEmail(self.__browser)
        self.new_email = NewEmail(self.__browser)
        self.send_status = SendStatus(self.__browser)

    def open_self(self):
        self.__browser.get(self.URL)

    def close_self(self):
        self.__browser.quit()