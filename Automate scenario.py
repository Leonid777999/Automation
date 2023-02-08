from selenium import webdriver

browser = webdriver.Chrome()
login = "/html/body/div[5]/div[3]/div[3]/div[2]/div[1]/div[3]/form/ul/li[1]/p[2]/input"
password = "/html/body/div[5]/div[3]/div[3]/div[2]/div[1]/div[3]/form/ul/li[1]/input"
open_site = browser.get("https://www.i.ua")
