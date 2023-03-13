from selenium.webdriver.common.by import By
from pages.po_base_class import BaseClass
from pages.po_send_status_page import Send_status
from locators.locators import Locators

class New_Email(BaseClass):

    def __init__(self, browser):
        super().__init__(browser)

    def fill_the_receiver_field(self, recevier:str):
        self.fill_the_field(Locators.FIELD_TO, recevier)
        return self
    def fill_the_subject_field(self, subject:str):
        self.fill_the_field(Locators.FIELD_SUBJECT, subject)
        return self
    def fill_the_text_field(self, text:str):
        self.fill_the_field(Locators.FIELD_TEXT, text)
        return self

    def click_send_mail_button(self):
        self.click_button(Locators.SEND_MAIL_BUTTON)
        return self


    def create_new_mail(self,receiver:str, subject:str, text:str):
        self.fill_the_receiver_field(receiver)
        self.fill_the_subject_field(subject)
        self.fill_the_text_field(text)
        self.click_send_mail_button()
        return Send_status(self.browser)


