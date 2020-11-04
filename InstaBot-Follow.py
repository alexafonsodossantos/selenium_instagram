from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time


instagram_username = "Your instagram username"
instagram_password = "Your instagram password"

PATH = "C:\Program Files (x86)\chromedriver.exe"

driver = webdriver.Chrome(PATH)

driver.get("https://instagram.com")


time.sleep(5)

searchUsername = driver.find_element_by_name('username')
searchPassword = driver.find_element_by_name('password')

searchUsername.send_keys(instagram_username)
searchPassword.send_keys(instagram_password)

searchPassword.send_keys(Keys.RETURN)

time.sleep(5)
skipSave = driver.find_element_by_xpath("//*[contains(text(), 'Agora não')]").click()

time.sleep(5)
skipNotifications = driver.find_element_by_xpath("//*[contains(text(), 'Agora não')]").click()

hashtag = "Programação"

driver.get("https://www.instagram.com/explore/tags/"+hashtag+"/")
time.sleep(5)

firstPost = driver.find_element_by_xpath("/html/body/div[1]/section/main/article/div[1]/div/div/div[1]/div[1]/a/div").click()
time.sleep(4)

followFirst = driver.find_element_by_xpath("/html/body/div[5]/div[2]/div/article/header/div[2]/div[1]/div[2]/button").click()
firstNext = driver.find_element_by_xpath("/html/body/div[5]/div[1]/div/div/a").click()
time.sleep(2)

maxFollows = 10

i = 0
while i < maxFollows:
    time.sleep(4)
    nextPage = driver.find_element_by_xpath("/html/body/div[5]/div[1]/div/div/a[2]").click()
    time.sleep(3)
    nextFollow = driver.find_element_by_xpath("/html/body/div[5]/div[2]/div/article/header/div[2]/div[1]/div[2]/button").click()
    i = i + 1

