from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

#Cria a função de login no instagram

def Login(driver, username, password):

    #busca os campos de usuário e senha 
    searchUsername = driver.find_element_by_name('username')
    searchPassword = driver.find_element_by_name('password')

    #preenche os campos, pressiona enter e aguarda 5 segundos.
    searchUsername.send_keys(username)
    searchPassword.send_keys(password)
    searchPassword.send_keys(Keys.RETURN)
    time.sleep(5)


#Cria a função que pula as janelas de salvar login e ativar notificações
def Skip(driver):
    skipSave = driver.find_element_by_xpath("//*[contains(text(), 'Agora não')]").click()
    time.sleep(5)
    skipNotifications = driver.find_element_by_xpath("//*[contains(text(), 'Agora não')]").click()

#Cria a função que segue x contas nos trendings da hashtag pesquisada
def FollowTrending(driver, hashtag, maxFollows):

    #abre a guia explore da hashtag selecionada
    driver.get("https://www.instagram.com/explore/tags/"+hashtag+"/")
    time.sleep(5)

    #encontra e abre o primeiro post, aguarda 4 segundos
    firstPost = driver.find_element_by_xpath("/html/body/div[1]/section/main/article/div[1]/div/div/div[1]/div[1]/a/div").click()
    time.sleep(4)

    #segue a conta do primeiro post
    followFirst = driver.find_element_by_xpath("/html/body/div[5]/div[2]/div/article/header/div[2]/div[1]/div[2]/button").click()
    
    #avança para o próximo post
    firstNext = driver.find_element_by_xpath("/html/body/div[5]/div[1]/div/div/a").click()
    time.sleep(2)


    i = 0
    while i < maxFollows:

        time.sleep(4)
        # segue a conta
        nextPage = driver.find_element_by_xpath("/html/body/div[5]/div[1]/div/div/a[2]").click()
        time.sleep(3)

        # avança para próxima
        nextFollow = driver.find_element_by_xpath("/html/body/div[5]/div[2]/div/article/header/div[2]/div[1]/div[2]/button").click()
        
        #incrementa a variável do loop
        i = i + 1


#Cria a função que curte x posts nos trendings
def LikeTrending(driver, hashtag, maxLikes):
    #abre a guia explore da hashtag selecionada
    driver.get("https://www.instagram.com/explore/tags/"+hashtag+"/")
    time.sleep(5)

    #abre o primeiro post
    firstPost = driver.find_element_by_xpath("/html/body/div[1]/section/main/article/div[1]/div/div/div[1]/div[1]/a/div").click()
    time.sleep(2)

    #curte o primeiro post
    firstLike = driver.find_element_by_xpath("/html/body/div[5]/div[2]/div/article/div[3]/section[1]/span[1]/button").click()
    time.sleep(2)

    #avança para o próximo
    firstNext = driver.find_element_by_xpath("/html/body/div[5]/div[1]/div/div/a").click()
    time.sleep(2)

    i = 0
    while i < maxLikes:
        
        #curte o post
        time.sleep(4)
        nextPage = driver.find_element_by_xpath("/html/body/div[5]/div[2]/div/article/div[3]/section[1]/span[1]/button").click()
        time.sleep(3)
        
        #avança para o próximo
        nextLike = driver.find_element_by_xpath("/html/body/div[5]/div[1]/div/div/a[2]").click()
        i = i + 1