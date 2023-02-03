from abc import (ABC, abstractmethod)
from selenium import webdriver

class A(ABC):
    def __init__(self):
        pass


    @abstractmethod
    def open_git(self):
        pass

    @abstractmethod
    def print_url(self):
        pass

class B(A):
    def __init__(self,url):
        super().__init__()
        self.url = url



class C(A):
    def __init__(self,url1):
        super().__init__()
        self.url1 = url1

    def open_git(self):
        browser = webdriver.Chrome()
        return browser.get(self.url1)

    def print_url(self):
        print(self.url1)



b = B()
b.print_url()

c =C("https://www.github.com")
c.open_git()
c.print_url()