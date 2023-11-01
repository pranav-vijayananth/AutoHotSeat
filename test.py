## USE THIS: https://stackoverflow.com/questions/24464631/authentication-with-selenium-python ##

from selenium import webdriver
from selenium.webdriver.common.by import By

url = "https://mail.google.com/mail/u/0/#inbox"

driver = webdriver.Chrome()

driver.get(url)

title = driver.title

print(title)

# driver.implicitly_wait(0.5)

driver.quit()