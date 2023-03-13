from selenium.webdriver.common.by import By
from Pages.po_base_class import BaseClass

class Send_status(BaseClass):

    def __init__(self, browser):
        super().__init__(browser)

    sended_mails_folder_button = By.XPATH, "//div[@class='block_gamma folders']/div[3]/ul/li[2]"
    sended_mail = By.XPATH, "//span[contains (text(), 'check the mail')]"

    def open_sended_mails_folder(self):
        self.click_button(self.sended_mails_folder_button)
        return self

    def get_title_of_sended_mail(self):
        get_title = self.get_text(self.sended_mail)
        return get_title


