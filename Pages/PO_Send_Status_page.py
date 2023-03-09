from selenium.webdriver.common.by import By
from Pages.PO_Base_Class import BaseClass
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class Send_status(BaseClass):

    def __init__(self, browser):
        super().__init__(browser)

    sended_mails_button = By.XPATH, "//div[@class='block_gamma folders']/div[3]/ul/li[2]"
    sended_mail = By.XPATH, "//span[contains (text(), 'check the mail')]"


    def open_sended_email_folder(self, open_folder):
        open = WebDriverWait(self.browser, 20).until(
            EC.presence_of_element_located(open_folder))
        return open.click()

    def get_email_title(self,email):
        title_get = WebDriverWait(self.browser, 20).until(
            EC.presence_of_element_located(email))
        return title_get.text