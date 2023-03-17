from selenium.webdriver.common.by import By


class LoginPageLocators:

    USER_LOGIN: tuple = By.XPATH, "//input[@name='login']"
    USER_PASSWORD: tuple = By.XPATH, "//input[@name='pass']"
    ENTER_BUTTON: tuple = By.XPATH, "//input[@tabindex='5']"
