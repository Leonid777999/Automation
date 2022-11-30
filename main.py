from selenium import webdriver
driver = webdriver.Chrome()
driver.get(url="https://www.jetbrains.com/help/pycharm/manage-branches.html")
print("test commit")