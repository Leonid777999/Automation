# 1.
class Test:
    type_m = "mobile application"
    type_w = "web application"

    def __init__(self, url, login, password):
        self.url = url
        self.login = login
        self.password = password
#2.
    def __str__(self):
        return f"({self.url, self.login, self.password})"

aa = Test("www.test.com", "entry", 123)

print(aa)

