from selenium.webdriver.common.by import By
class Locators:

    #login page
    USER_LOGIN: tuple = By.XPATH, "//input[@name='login']"
    USER_PASSWORD: tuple = By.XPATH, "//input[@name='pass']"
    ENTER_BUTTON: tuple = By.XPATH, "//input[@tabindex='5']"

    #mailbox page
    EMAIL_FIRST: tuple = By.XPATH, "//span[contains(text(), 'Осторожно мошенники!')]"
    EMAIL_SECOND: tuple  = By.XPATH, "//span[contains(text(), 'Рекомендации по безопасности Вашего аккаунта')]"
    EMAIL_ROW_TO_OPEN: tuple  = By.XPATH, "//span[contains(text(), 'Осторожно мошенники!')]"

    #current email page
    EMAIL_SUBJECT: tuple = By.XPATH, "//div[@class='message_header iua_support clear']/h3"
    EMAIL_SENDER: tuple = By.XPATH, "//div[@class='from']/div[2]/a"
    EMAIL_RECEIVER: tuple = By.XPATH, "//div[@class='to']/div[2]"
    CREATE_NEW_MAIL_BUTTON: tuple = By.XPATH, "//p[@class='make_message']/a"

    #new email page
    FIELD_TO: tuple = By.ID, "to"
    FIELD_SUBJECT: tuple = By.XPATH, "//input[@name='subject']"
    FIELD_TEXT: tuple = By.ID, "text"
    SEND_MAIL_BUTTON: tuple = By.XPATH, "//input[@type='submit']"

    #send status page
    SENDED_MAILS_FOLDER_BUTTON: tuple = By.XPATH, "//div[@class='block_gamma folders']/div[3]/ul/li[2]"
    SENDED_MAIL: tuple = By.XPATH, "//span[contains (text(), 'check the mail')]"




