from selenium import webdriver
browser = webdriver.Chrome()

site = "https://www.i.ua"
login = "//input[@name='login']"
password = "//input[@name='pass']"
enter = "//input[@tabindex='5']"


def open_site():
    open = browser.get(site)
    return open


