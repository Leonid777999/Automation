from selenium import webdriver

browser = webdriver.Chrome()

site = "https://www.i.ua"
login = browser.find_element("xpath","//input[@name='login']")
password = browser.find_element("xpath","//input[@name='pass']")
enter = browser.find_element("xpath","//input[@tabindex='5']")


def open_site():
    return browser.get(site)

def type_login():
    return login.send_keys()


