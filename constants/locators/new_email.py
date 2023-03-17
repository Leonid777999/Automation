from selenium.webdriver.common.by import By


class NewEmailLocators:

    FIELD_TO: tuple = By.ID, "to"
    FIELD_SUBJECT: tuple = By.XPATH, "//input[@name='subject']"
    FIELD_TEXT: tuple = By.ID, "text"
    SEND_MAIL_BUTTON: tuple = By.XPATH, "//input[@type='submit']"
