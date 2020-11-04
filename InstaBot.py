from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
from assets import Skip, Login, FollowTrending, LikeTrending

#carrega usuário e senha do arquivo pass.txt
f = open("pass.txt", "r")

#define as variaveis instagram_username e instagram_password com o valor da primeira e segunda linha do arquivo
instagram_username = f.readline()
instagram_password = f.readline()

#define o PATH do chromewebdriver
PATH = "C:\Program Files (x86)\chromedriver.exe"

#cria o driver
driver = webdriver.Chrome(PATH)

#vai para a página inicial do instagram
driver.get("https://instagram.com")

time.sleep(5)

#Realiza o login
Login(driver, instagram_username, instagram_password)

#Pula a opção de salvar senha e exibir notificações (comente a próxima linha caso não seja necessário no seu ambiente)
Skip(driver)

#Chama a função para seguir x contas nos resultados da busca por hashtag
FollowTrending(driver, "pythonprogramming", 2)

#Chama a função para curtir x posts nos resultados da busca por hashtag
LikeTrending(driver, "Dev", 2)