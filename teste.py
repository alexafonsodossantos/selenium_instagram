from selenium.webdriver import Chrome
import time
from selenium.webdriver.common.keys import Keys


url = "https://instagram.com"

PATH = "C:\Program Files (x86)\chromedriver.exe"

navegador = Chrome(PATH)

navegador.get(url)

search = navegador.find_elements_by_name("username")

search.send_keys("thebluesbassman")



