from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

def login(driver, username, password):
    searchUsername = driver.find_element_by_name('username')
    searchPassword = driver.find_element_by_name('password')

    searchUsername.send_keys(username)
    searchPassword.send_keys(password)

    searchPassword.send_keys(Keys.RETURN)
