from selenium.webdriver.common.by import By



class MailBoxLocators:

    EMAIL_FIRST: tuple = By.XPATH, "//span[contains(text(), 'Осторожно мошенники!')]"
    EMAIL_SECOND: tuple = By.XPATH, "//span[contains(text(), 'Рекомендации по безопасности Вашего аккаунта')]"
    EMAIL_ROW_TO_OPEN: tuple = By.XPATH, "//span[contains(text(), 'Осторожно мошенники!')]"
    MESSAGE_LIST: list = By.XPATH, "//span[@class='sbj']"