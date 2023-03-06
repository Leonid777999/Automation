from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
class BaseClass:

    def __init__(self,browser):
        self.browser = browser
        self.wait = WebDriverWait(self.browser,10)




