from selenium.webdriver.common.by import By
from Pages.Page_Object_Base_Class import BaseClass
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC



class MailBox(BaseClass):

    def __init__(self, browser):
        super().__init__(browser)

    email_last = By.XPATH, "//*[@id='mesgList']/form/div[1]/a/span[3]/span"
    email_before_the_last = By.XPATH, "//*[@id='mesgList']/form/div[2]/a/span[3]/span"
    email_row_to_open = By.XPATH, "//div[@class ='row _last']"

    def get_email_title(self,email):
        title_get = WebDriverWait(self.browser, 20).until(
            EC.presence_of_element_located(email))
        return title_get.text
    def open_email(self):
        element_open = WebDriverWait(self.browser, 20).until(
            EC.presence_of_element_located(self.email_row_to_open))
        return element_open.click()


class CurrentEmail(BaseClass):

    email_subject = By.XPATH, "/html/body/div[1]/div[6]/div[2]/div[2]/ul/li/div[1]/div/div[2]/h3"
    email_sender = By.XPATH, "/html/body/div[1]/div[6]/div[2]/div[2]/ul/li/div[1]/div/div[2]/div[1]/div[2]/a"
    email_reciever = By.XPATH, "/html/body/div[1]/div[6]/div[2]/div[2]/ul/li/div[1]/div/div[2]/div[2]/div[2]"
    create_button = By.XPATH, "//p[@class='make_message']/a"

    def __init__(self,browser):
        super().__init__(browser)

    def get_email_data(self, email):
        element = WebDriverWait(self.browser, 20).until(
          EC.presence_of_element_located(email))
        return element.text

    def click_on_create_button(self,link_to_button):
        create_button = WebDriverWait(self.browser, 20).until(
            EC.presence_of_element_located(link_to_button))
        return create_button.click()



