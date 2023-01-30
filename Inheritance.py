from classes import Test
from selenium import webdriver

class Web(Test):
    platform = "Chrome"
    browser = webdriver.Chrome()


    def __init__(self, new_login, url, login, password):
        super().__init__(url, login, password)
        self.new_login = new_login
    def make_choice(self):
        choice1 = input("Your choice:")
        if choice1 == super().type:
            choice2 = input("Your platform")
            if choice2 == Web.platform:
                print("You are welcome!")
            else:
                print("Ask another team!")
        else:
            print("Ask another team!")

    def go_to(self):
        return Web.browser.get(self.url)

    def extra_login(self):
        extra_login = super().new_login() + "55+"
        return extra_login


obj = Web("mobile","https://www.github.com","login","password")
thor1 = Web("mob","https://www.github.com", "login", 56788)

# check for the task 2
thor1.make_choice()

thor1.extra_login()

thor1.new_password(10000)

thor1.new_login()




