from PageObjectBaseClass import BaseClass
class LoginPage(BaseClass):

    def __init__(self, browser):
        super().__init__(browser)

    user_login = "xpath","//input[@name='login']"
    user_password = "xpath","//input[@name='pass']"
    enter = "xpath","//input[@tabindex='5']"


    def enter_user_login(self,login):
        self.browser.find_element(*self.user_login).send_keys(login)



