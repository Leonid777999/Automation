from selenium.webdriver.common.by import By


class MailStatusLocators:

    SENT_MAILS_FOLDER_BUTTON: tuple = By.XPATH, "//a[contains (text(), 'Отправленные')]"
