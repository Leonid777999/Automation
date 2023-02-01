#1 111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111
class First:

    def __init__(self, first_protected, first_private):
        self._first_protected = first_protected
        self.__first_private = first_private

    def _protected_method(self):
        return self.__dict__

    def __private_method(self):
        return self.__dict__

#2 2222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222
class Second:
    def __init__(self, first_protected,first_private,second_public):
        super().__init__(first_protected,first_private,second_public)
        self.second_public = second_public



second = Second("protected", "private", "public")
second.first_protected

#3 33333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333

first = First("protected", "private")

first._first_protected = "protected1"
first._First__first_private = "private1"

first._first_protected
first._First__first_private

first._protected_method()
first._First__private_method()



