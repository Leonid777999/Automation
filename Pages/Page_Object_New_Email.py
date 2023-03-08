from selenium.webdriver.common.by import By
from Pages.Page_Object_Base_Class import BaseClass
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class New_Email(BaseClass):

    def __init__(self, browser):
        super().__init__(browser)

    field_to = By.ID, "to"
    field_text = By.ID, "text"
    field_subject = By.XPATH, "//input[@name='subject']"
    send_mail_button = By.XPATH, "//input[@type='submit']"
    folder_with_sended_button = By.XPATH, "//li[@class='current']/a"

    def fill_the_field(self, field, text: str):
        fill_field = WebDriverWait(self.browser, 20).until(
            EC.presence_of_element_located(field))
        return fill_field.send_keys(text)

    def send_email(self, send_button):
        send = WebDriverWait(self.browser, 20).until(
            EC.presence_of_element_located(send_button))
        return send.click()