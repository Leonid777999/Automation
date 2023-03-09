from selenium.webdriver.common.by import By
from Pages.PO_Base_Class import BaseClass

class New_Email(BaseClass):

    def __init__(self, browser):
        super().__init__(browser)

    field_to = By.ID, "to"
    field_text = By.ID, "text"
    field_subject = By.XPATH, "//input[@name='subject']"
    send_mail_button = By.XPATH, "//input[@type='submit']"
    folder_with_sended_button = By.XPATH, "//li[@class='current']/a"



