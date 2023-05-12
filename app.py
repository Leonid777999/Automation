from selenium import webdriver
from pages.po_login_page import LoginPage
from pages.po_mailbox_page import MailBox, CurrentEmail
from pages.po_new_email_page import NewEmail
from pages.po_mail_status_page import MailStatus
from pages.sent_mail_folder import SentMailFolder


class App:

    URL = "https://www.i.ua/"

    def __init__(self, headless=False):

        self.__browser = webdriver.Chrome()
        if headless == "--headless":





        self.login_page = LoginPage(self.__browser)
        self.mailbox_page = MailBox(self.__browser)
        self.current_email = CurrentEmail(self.__browser)
        self.new_email = NewEmail(self.__browser)
        self.send_status = MailStatus(self.__browser)
        self.sent_mail = SentMailFolder(self.__browser)

    def open(self):
        self.__browser.get(self.URL)

    def close(self):
        self.__browser.quit()