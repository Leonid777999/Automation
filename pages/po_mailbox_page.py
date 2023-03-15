from pages.po_base_class import BaseClass
from pages.po_new_email_page import NewEmail
from locators.locators import Locators

class MailBox(BaseClass):

    def __init__(self, browser):
        super().__init__(browser)

    def get_title_first_mail(self):
        get_title = self.get_text(Locators.EMAIL_FIRST)
        return get_title

    def get_title_second_mail(self):
        get_title = self.get_text(Locators.EMAIL_SECOND)
        return get_title
    def open_email(self):
        self.click_button(Locators.EMAIL_ROW_TO_OPEN)



class CurrentEmail(BaseClass):

    def __init__(self,browser):
        super().__init__(browser)

    def get_data_from_subject(self):
        get_subject = self.get_text(Locators.EMAIL_SUBJECT)
        return get_subject

    def get_data_from_sender(self):
        get_sender = self.get_text(Locators.EMAIL_SENDER)
        return get_sender

    def get_data_from_receiver(self):
        get_receiver = self.get_text(Locators.EMAIL_RECEIVER)
        return get_receiver

    def create_new_mail(self):
        self.click_button(Locators.CREATE_NEW_MAIL_BUTTON)
        return NewEmail(self.browser)



