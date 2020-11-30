#url = 'https://www.terabyteshop.com.br/busca?str=rx+6800+16GB'
import os
from logging import log
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import os
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException, StaleElementReferenceException

from playsound import playsound

def cls():
    os.system('cls' if os.name=='nt' else 'clear')

def enterSite():
    url = ''
    DRIVER_PATH = 'chromedriver.exe'
    options = Options()
    driver = webdriver.Chrome(options=options, executable_path=DRIVER_PATH)
    options.add_argument("--window-size=1920,1200")
    driver.get(url)
    return driver



def procurarProdutosTera(driver):
    produtos = []
    login = driver.find_elements_by_xpath("""//*[@id="prodarea"]/div""")    #pegar o nome e o preço e ver se tem RX 6800 na string
    cls()
    print('****************************************************************************************TERABY***************************************************************************************')
    inicio = 1
    for x in login:
        if x.get_attribute("class") == 'pbox col-xs-12 col-sm-6 col-md-3':
            produtos.append(x)
    ignored_exceptions=(NoSuchElementException,StaleElementReferenceException,)
    firstProduto = 1
    for p in produtos: #//*[@id="prodarea"]/div[1]/div/div[4]
        nome = p.find_element_by_xpath("""//*[@id="prodarea"]/div["""+str(produtos.index(p)+1)+"""]/div/div[3]/a/h2/strong""").text
        if 'TODOS VENDIDOS' in p.find_element_by_xpath("""//*[@id="prodarea"]/div[1]/div/div[4]""").text:
            print("Modelo: %-*s  Status: %s" % (100,nome," | Indisponível"))