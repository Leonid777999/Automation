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

#3.
    def make_choice(self):
        choice = input("Your choice:")
        ad = 5
        if choice == Test.type_m:
            print("You are welcome")
        else:
            print("Ask another team")

    def new_login(self):
        new_login = self.login + str(1)
        return new_login

    def new_password(self,add):
        new_password = self.password + int(add)
        return new_password


#4.
test_object = Test("www.test.com", "entry", 123)
test_object1 = Test("www.test111", "comeon", 234)

# check for the second task
print(test_object)

# check for the third task
test_object.make_choice()

test_object.new_login()

test_object1.new_password(456)

#5
setattr(test_object,"login","new entry")
getattr(test_object,"login")

#6
setattr(test_object1,"captcha","true")
getattr(test_object1,"captcha")
print(test_object1)     #??? how to print current object with the added attribute


