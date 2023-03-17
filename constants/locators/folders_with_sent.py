from selenium.webdriver.common.by import By


class SentMailFolderLocators:

    SENT_MAIL: tuple = By.XPATH, "//span[contains (text(), 'check the mail')]"
