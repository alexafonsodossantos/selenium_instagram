from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time


instagram_username = "thebluesbassman"
instagram_password = "Ab742853964"

PATH = "C:\Program Files (x86)\chromedriver.exe"

driver = webdriver.Chrome(PATH)

driver.get("https://instagram.com")


time.sleep(5)

searchUsername = driver.find_element_by_name('username')
searchPassword = driver.find_element_by_name('password')

searchUsername.send_keys(instagram_username)
searchPassword.send_keys(instagram_password)

searchPassword.send_keys(Keys.RETURN)

time.sleep(3)
buttons = driver.find_element_by_xpath("//*[contains(text(), 'Agora não')]").click()

time.sleep(4)
buttons2 = driver.find_element_by_xpath("//*[contains(text(), 'Agora não')]").click()

driver.get("https://instagram.com/explore")