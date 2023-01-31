class First:

    def __init__(self, first_protected, first_private):
        self._first_protected = first_protected
        self.__first_private = first_private

    def _protected_method(self):
        return self.__dict__

    def __private_method(self):
        return self.__dict__





first = First("protected", "private")

first._first_protected
first._First__first_private

first._protected_method()