from selenium.webdriver.common.by import By


class LoginLocators:

    USER_LOGIN: tuple = By.XPATH, "//input[@name='login']"
    USER_PASSWORD: tuple = By.XPATH, "//input[@name='pass']"
    ENTER_BUTTON: tuple = By.XPATH, "//input[@tabindex='5']"
