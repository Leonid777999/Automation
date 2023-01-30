# 1.
class Test:
    type = "web application"

    def __init__(self,url, login, password):
        self.url = url
        self.login = login
        self.password = password
#2.
    def real_print(cls):
        return str(f"({cls.url, cls.login, cls.password})")

#3.
    def make_choice(self):
        choice = input("Your choice:")
        if choice == Test.type:
            print("You are welcome")
        else:
            print("Ask another team")

    def new_login(self):
        new_login = str(self.login) + str(8)
        return new_login

    def new_password(self,add):
        new_password = self.password + int(add)
        return new_password

    def print_new(self):
        return f"({self})"



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

setattr(test_object,"login","new entry")

#6
test_object.new = "new variable"
print(test_object.__dict__)

setattr(test_object1,"captcha","true")
getattr(test_object1,"captcha")

test_object.print_new()     #??? how to print current object with the added attribute without key

