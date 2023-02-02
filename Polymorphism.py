class First:
    def __init__(self,url, login, password):
        self.url = url
        self.login = login
        self.password = password

    def new_login(self):
        new_login = str(self.login) + "8"
        return new_login


class Second:
    def __init__(self,url1, login1, password1):
        self.url1 = url1
        self.login1 = login1
        self.password1 = password1


    def new_login(self, add):
        new_login = self.login1 + int(add)
        return new_login



class Third:
    def __init__(self,url2, login2, password2):
        self.url2 = url2
        self.login2 = login2
        self.password2 = password2

    def new_login(self):
        print (f"({self.url2, self.login2, self.password2}")


