from selenium.webdriver.common.by import By
from Pages.PO_Base_Class import BaseClass
from Pages.PO_Send_Status_page import Send_status

class New_Email(BaseClass):

    def __init__(self, browser):
        super().__init__(browser)

    field_to = By.ID, "to"
    field_subject = By.XPATH, "//input[@name='subject']"
    field_text = By.ID, "text"
    send_mail_button = By.XPATH, "//input[@type='submit']"
    folder_with_sended_button = By.XPATH, "//li[@class='current']/a"

    def fill_the_receiver_field(self, recevier:str):
        self.fill_the_field(self.field_to, recevier)
        return self
    def fill_the_subject_field(self, subject:str):
        self.fill_the_field(self.field_subject, subject)
        return self
    def fill_the_text_field(self, text:str):
        self.fill_the_field(self.field_text, text)
        return self

    def click_send_mail_button(self):
        self.click_button(self.send_mail_button)
        return self


    def create_new_mail(self,receiver:str, subject:str, text:str):
        self.fill_the_receiver_field(receiver)
        self.fill_the_subject_field(subject)
        self.fill_the_text_field(text)
        self.click_send_mail_button()
        return Send_status(self.browser)


