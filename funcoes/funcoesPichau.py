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

def enterSite(url):
    url = 'https://www.pichau.com.br/hardware/placa-de-video?rgpu=6336%2C6337'
    DRIVER_PATH = 'chromedriver.exe'
    options = Options()
    options.headless = True
    driver = webdriver.Chrome(options=options, executable_path=DRIVER_PATH)
    options.add_argument("--window-size=1920,1200")
    driver.get(url)
    return driver
#
def procurarProdutosPichau(driver):
    produtos = []
    disponiveis=[]
    login = driver.find_elements_by_xpath("""//*[@id="amasty-shopby-product-list"]/div[2]/ol/li""")    #pegar o nome e o preço e ver se tem RX 6800 na string
    cls()
    print('****************************************************************************************PICHAU***************************************************************************************')
    inicio = 1
    for x in login:
        if x.get_attribute("class") == 'item product product-item':
            #print(x.text)
            produtos.append(x)
        else:
            print('**div não é um produto**')

    ignored_exceptions=(NoSuchElementException,StaleElementReferenceException,)
    firstProduto = 1
    for p in produtos:
        xnomePlaca = """//*[@id="amasty-shopby-product-list"]/div[2]/ol/li[""" + str(produtos.index(p)+1) + """]/div/div/strong/a"""
        nome = WebDriverWait(driver, 10,ignored_exceptions=ignored_exceptions).until(EC.presence_of_element_located((By.XPATH, xnomePlaca))) #botao comprar
        if "PRODUTO INDISPONÍVEL" in p.text:
            print("Modelo: %-*s  Status: %s" % (150,nome.text," | Indisponível"))
        else:
            print("Modelo: %-*s  Status: %s" % (150,nome.text," | Indisponível"))
            disponiveis.append(p)
            playsound('C:/Users/power/bot/trem.wav')
    print("Temos ", len(disponiveis), " produtos que atendem a esses requisitos")