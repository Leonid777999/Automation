class First:
    def __init__(self, url, login, password):
        self.url = url
        self.login = login
        self.password = password

    def new_login(self):
        new_login = str(self.login) + "8"
        return new_login


class Second:
    def __init__(self, url1, login1, password1):
        self.url1 = url1
        self.login1 = int(login1)
        self.password1 = password1

    def new_login(self, add):
        new_login = self.login1 + int(add)
        return new_login


class Third:
    def __init__(self, url2, login2, password2):
        self.url2 = url2
        self.login2 = login2
        self.password2 = password2

    def new_login(self):
        print(f"({self.url2, self.login2, self.password2}")


# 2 2222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222
def polymorph():
    print(first.new_login())
    print(second.new_login(5))
    third.new_login()


# 3 3333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333

first = First("url", "login", "password")
second = Second("url1", 10, "password1")
third = Third("url2", "login2", "password2")

def polymorph1(first,second,third):
    print(first.__dict__)
    print(second.__dict__)
    print(third.__dict__)

polymorph1(first, second, third)