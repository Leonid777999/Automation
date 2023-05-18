from selenium import webdriver
from pages.po_login_page import LoginPage
from pages.po_mailbox_page import MailBox, CurrentEmail
from pages.po_new_email_page import NewEmail
from pages.po_mail_status_page import MailStatus
from pages.sent_mail_folder import SentMailFolder



class App:

    URL = "https://www.i.ua/"
    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_argument('headless')
    firefox_options = webdriver.FirefoxOptions()
    firefox_options.add_argument('headless')

    def __init__(self, browser: str, headless=False):

        browser_type = browser.lower()
        if browser_type == 'firefox':
            if headless == 'headless':
                self.__browser = webdriver.Firefox(options=self.firefox_options)
            else:
                self.__browser = webdriver.Firefox()
        elif browser_type == 'chrome':
            if headless == 'headless':
                self.__browser = webdriver.Chrome(options=self.chrome_options)
            else:
                self.__browser = webdriver.Chrome()
        else:
            self.__browser = webdriver.Chrome()

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

