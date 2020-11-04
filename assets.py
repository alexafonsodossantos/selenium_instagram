from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time


def Login(driver, username, password):
    searchUsername = driver.find_element_by_name('username')
    searchPassword = driver.find_element_by_name('password')
    searchUsername.send_keys(username)
    searchPassword.send_keys(password)
    searchPassword.send_keys(Keys.RETURN)
    time.sleep(5)

def Skip(driver):
    skipSave = driver.find_element_by_xpath("//*[contains(text(), 'Agora não')]").click()
    time.sleep(5)
    skipNotifications = driver.find_element_by_xpath("//*[contains(text(), 'Agora não')]").click()



def FollowTrending(driver, hashtag, maxFollows):


    driver.get("https://www.instagram.com/explore/tags/"+hashtag+"/")
    time.sleep(5)

    firstPost = driver.find_element_by_xpath("/html/body/div[1]/section/main/article/div[1]/div/div/div[1]/div[1]/a/div").click()
    time.sleep(4)

    followFirst = driver.find_element_by_xpath("/html/body/div[5]/div[2]/div/article/header/div[2]/div[1]/div[2]/button").click()
    firstNext = driver.find_element_by_xpath("/html/body/div[5]/div[1]/div/div/a").click()
    time.sleep(2)


    i = 0
    while i < maxFollows:
        time.sleep(4)
        nextPage = driver.find_element_by_xpath("/html/body/div[5]/div[1]/div/div/a[2]").click()
        time.sleep(3)
        nextFollow = driver.find_element_by_xpath("/html/body/div[5]/div[2]/div/article/header/div[2]/div[1]/div[2]/button").click()
        i = i + 1




def LikeTrending(driver, hashtag, maxLikes):
    driver.get("https://www.instagram.com/explore/tags/"+hashtag+"/")
    time.sleep(5)

    firstPost = driver.find_element_by_xpath("/html/body/div[1]/section/main/article/div[1]/div/div/div[1]/div[1]/a/div").click()
    time.sleep(2)

    firstLike = driver.find_element_by_xpath("/html/body/div[5]/div[2]/div/article/div[3]/section[1]/span[1]/button").click()
    time.sleep(2)
    firstNext = driver.find_element_by_xpath("/html/body/div[5]/div[1]/div/div/a").click()
    time.sleep(2)

    i = 0
    while i < maxLikes:
        time.sleep(4)
        nextPage = driver.find_element_by_xpath("/html/body/div[5]/div[2]/div/article/div[3]/section[1]/span[1]/button").click()
        time.sleep(3)
        nextLike = driver.find_element_by_xpath("/html/body/div[5]/div[1]/div/div/a[2]").click()
        i = i + 1