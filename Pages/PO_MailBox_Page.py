from selenium.webdriver.common.by import By
from Pages.PO_Base_Class import BaseClass

class MailBox(BaseClass):

    def __init__(self, browser):
        super().__init__(browser)

    email_first = By.XPATH, "//span[contains(text(), 'Осторожно мошенники!')]"
    email_second = By.XPATH, "//span[contains(text(), 'Рекомендации по безопасности Вашего аккаунта')]"
    email_row_to_open = By.XPATH, "//div[@class ='row _last']"



class CurrentEmail(BaseClass):

    email_subject = By.XPATH, "/html/body/div[1]/div[6]/div[2]/div[2]/ul/li/div[1]/div/div[2]/h3"
    email_sender = By.XPATH, "/html/body/div[1]/div[6]/div[2]/div[2]/ul/li/div[1]/div/div[2]/div[1]/div[2]/a"
    email_reciever = By.XPATH, "/html/body/div[1]/div[6]/div[2]/div[2]/ul/li/div[1]/div/div[2]/div[2]/div[2]"
    create_button = By.XPATH, "//p[@class='make_message']/a"


    def __init__(self,browser):
        super().__init__(browser)





