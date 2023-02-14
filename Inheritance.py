from classes import Test
from selenium import webdriver
import random
import string


class Web(Test):

    def __init__(self, next_login, url, login, password, type):
        super().__init__(url, login, password, type)
        self.next_login = next_login
    def make_choice(self):
        choice1 = input("Your choice:")
        if choice1 == self.type:
            platform = "chrome"
            choice2 = input("Your platform").lower()
            if choice2 == platform:
                print("You are welcome!")
            else:
                print("Ask another team!")
        else:
            print("Ask another team!")

    def go_to(self):
        browser = webdriver.Chrome()
        return browser.get(self.url)

    def extra_login(self):
        extra_login = self.new_login() + "55+"
        return extra_login


thor1 = Web("mob","https://www.github.com", "login", 56788, "web application")

#2  222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222
thor1.make_choice()

thor1.extra_login()

thor1.new_password(10000)

thor1.new_login()

#3 33333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333
class One:

    def __init__(self, login_one, password_one):
        self.login_one = login_one
        self.password_one = password_one

    def generator(self):
        next_login = self.login_one + "5"
        next_password = self.password_one + "10"
        return next_login,next_password

class Two:
    def __init__(self, key_two, token_two):
        self.key_two = key_two
        self. token_two = token_two

    def generator(self):
        next_key = self.key_two + random.choice(string.ascii_letters)
        next_token = self.token_two + random.choice(string.ascii_letters)
        return next_key, next_token

class Three(One, Two):
    def __init__(self, login_one, password_one):
        super().__init__(login_one, password_one)
    def printer(self):
        return f"{self.login_one,self.password_one}"


#4 4444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444

generator3 = Three("login", "password")

generator3.printer()

Three.mro()
generator3.generator()

