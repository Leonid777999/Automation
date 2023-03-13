from pages.po_login_page import LoginPage
from pages.po_mailbox_page import MailBox, CurrentEmail
from pages.po_new_email_page import New_Email
from pages.po_send_status_page import Send_status

class App:

    def __init__(self, browser):
        # broser init
        self.__browser = browser  # чи що ти там створюєш
        # PO init
        self.login_page = LoginPage(self.__browser)
        self.mailbox_page = MailBox(self.__browser)
        self.current_email = CurrentEmail(self.__browser)
        self.new_email = New_Email(self.__browser)
        self.send_status = Send_status(self.__browser)

