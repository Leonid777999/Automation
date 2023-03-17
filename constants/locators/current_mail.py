from selenium.webdriver.common.by import By


class CurrentMailLocators:

    EMAIL_SUBJECT: tuple = By.XPATH, "//div[@class='message_header iua_support clear']/h3"
    EMAIL_SENDER: tuple = By.XPATH, "//div[@class='from']/div[2]/a"
    EMAIL_RECEIVER: tuple = By.XPATH, "//div[@class='to']/div[2]"
    CREATE_NEW_MAIL_BUTTON: tuple = By.XPATH, "//p[@class='make_message']/a"

