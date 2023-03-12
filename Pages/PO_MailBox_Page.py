from selenium.webdriver.common.by import By
from Pages.PO_Base_Class import BaseClass
from Pages.PO_New_Email_Page import New_Email

class MailBox(BaseClass):

    def __init__(self, browser):
        super().__init__(browser)

    email_first = By.XPATH, "//span[contains(text(), 'Осторожно мошенники!')]"
    email_second = By.XPATH, "//span[contains(text(), 'Рекомендации по безопасности Вашего аккаунта')]"
    email_row_to_open = By.XPATH, "//span[contains(text(), 'Осторожно мошенники!')]"

    def get_title_first_mail(self):
        get_title = self.get_text(self.email_first)
        return get_title

    def get_title_second_mail(self):
        get_title = self.get_text(self.email_second)
        return get_title
    def open_email(self):
        self.click_button(self.email_row_to_open)



class CurrentEmail(BaseClass):

    email_subject = By.XPATH, "//div[@class='message_header iua_support clear']/h3"
    email_sender = By.XPATH, "//div[@class='from']/div[2]/a"
    email_receiver = By.XPATH, "//div[@class='to']/div[2]"
    create_button = By.XPATH, "//p[@class='make_message']/a"


    def __init__(self,browser):
        super().__init__(browser)

    def get_data_from_subject(self):
        get_subject = self.get_text(self.email_subject)
        return get_subject

    def get_data_from_sender(self):
        get_sender = self.get_text(self.email_sender)
        return get_sender

    def get_data_from_receiver(self):
        get_receiver = self.get_text(self.email_receiver)
        return get_receiver

    def create_new_mail(self):
        self.click_button(self.create_button)
        return New_Email(self.browser)



