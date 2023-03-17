from selenium.webdriver.common.by import By


class MailStatusLocators:

    SENT_MAILS_FOLDER_BUTTON: tuple = By.XPATH, "//div[@class='block_gamma folders']/div[3]/ul/li[2]"
