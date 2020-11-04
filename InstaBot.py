from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
from assets import Skip, Login, FollowTrending, LikeTrending

f = open("pass.txt", "r")

instagram_username = f.readline()
instagram_password = f.readline()

PATH = "C:\Program Files (x86)\chromedriver.exe"

driver = webdriver.Chrome(PATH)

driver.get("https://instagram.com")


time.sleep(5)


Login(driver, instagram_username, instagram_password)

Skip(driver)

FollowTrending(driver, "pythonprogramming", 2)

LikeTrending(driver, "Dev", 2)