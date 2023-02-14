# 1.
class Test:

    def __init__(self,url, login, password, type = "web_application"):
        self.url = url
        self.login = login
        self.password = password
        self.type = type
#2.
    def real_print(self):
        return str(f"({self.url, self.login, self.password})")

#3.
    def make_choice(self):
        choice = input("Your choice:")
        if choice == self.type:
            print("You are welcome")
        else:
            print("Ask another team")

    def new_login(self):
        new_login = str(self.login) + "8"
        return new_login

    def new_password(self,add):
        new_password = self.password + add
        return new_password





#4.
test_object = Test("www.test.com", "entry", 123)
test_object1 = Test("www.test111", "comeon", 234)

# check for the second task
print(test_object)



# check for the third task
test_object.make_choice()

test_object.new_login()

test_object1.new_password(459)

#5

test_object.login = "new login"



#6
test_object.new = "new variable"
print(test_object.__dict__)

test_object1.captcha = "true"
getattr(test_object1,"captcha")


