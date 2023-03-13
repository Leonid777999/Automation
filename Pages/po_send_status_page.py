from selenium.webdriver.common.by import By
from Pages.po_base_class import BaseClass

class Send_status(BaseClass):

    def __init__(self, browser):
        super().__init__(browser)

    sended_mails_button = By.XPATH, "//div[@class='block_gamma folders']/div[3]/ul/li[2]"
    sended_mail = By.XPATH, "//span[contains (text(), 'check the mail')]"




