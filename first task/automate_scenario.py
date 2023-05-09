# login = automate  , passwd = automate123
from selenium import webdriver


browser = webdriver.Chrome()
login = "//input[@name='login']"
password = "//input[@name='pass']"
enter = "//input[@tabindex='5']"
email_last = []
email_before_last = []

open_site = browser.get("https://www.i.ua")
browser.find_element("xpath",login).send_keys("1automate")
browser.find_element("xpath",password).send_keys("automate123")
browser.find_element("xpath",enter).click()
find_email1 = browser.find_element("xpath","//*[@id='mesgList']/form/div[1]/a/span[3]/span")
find_email2 = browser.find_element("xpath","//*[@id='mesgList']/form/div[2]/a/span[3]/span")
email_last.append(find_email1.text)
email_before_last.append(find_email2.text)

print(email_last)
print(email_before_last)




