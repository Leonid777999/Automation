from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
class BaseClass:

    def __init__(self,browser):
        self.browser = browser
        self.wait = WebDriverWait(self.browser, 20)

    def get_text_data(self, position):
        get_data = self.wait.until(EC.presence_of_element_located(position))
        return get_data.text

    def click_button(self, button):
        click = self.wait.until(EC.presence_of_element_located(button))
        return click.click()

    def fill_the_field(self, field, text:str):
        fill = self.wait.until(EC.presence_of_element_located(field))
        return fill.send_keys(text)



