# login = automate  , passwd = automate123
from selenium import webdriver

browser = webdriver.Chrome()
login = "/html/body/div[5]/div[3]/div[3]/div[2]/div[1]/div[3]/form/ul/li[1]/p[2]/input"
password = "/html/body/div[5]/div[3]/div[3]/div[2]/div[1]/div[3]/form/ul/li[1]/input"
enter = "/html/body/div[5]/div[3]/div[3]/div[2]/div[1]/div[3]/form/p/input"
open_site = browser.get("https://www.i.ua")
browser.find_element("xpath","/html/body/div[3]/div[3]/div[3]/div[2]/div[1]/div[3]/form/ul/li[1]/p[2]/input").send_keys("automate")
browser.find_element("name","pass").send_keys("automate123")
browser.find_element("xpath","//p/input").click()







