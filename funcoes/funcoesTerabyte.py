from logging import log
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException, StaleElementReferenceException
from Metodos.metodos import *
from playsound import playsound
import threading
from threading import Thread

cls()

def tocarSom():
    return playsound('alert.mp3', block = False)
    

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
    print('****************************************************************************************Terabyte Shop***************************************************************************************')
    for x in login:
        if x.get_attribute("class") == 'pbox col-xs-12 col-sm-6 col-md-3':
            produtos.append(x)
    ignored_exceptions=(NoSuchElementException,StaleElementReferenceException,)
    for p in produtos: #//*[@id="prodarea"]/div[1]/div/div[4]
        #nome = p.find_element_by_xpath("""//*[@id="prodarea"]/div["""+str(produtos.index(p)+1)+"""]/div/div[3]/a/h2/strong""").text
        nome = p.text
        if 'TODOS VENDIDOS' in p.find_element_by_xpath("""//*[@id="prodarea"]/div[1]/div/div[4]""").text:
            print(bcolors.BOLD + "Modelo:" + bcolors.ENDC + "%-*s    %s"% (150,nome, bcolors.BOLD + "Status:" + bcolors.FAIL + " Indisponível" + bcolors.ENDC))
        if "PC" in nome:
            continue
        else:
            print (bcolors.BOLD + "Modelo:" + bcolors.ENDC + "%-*s    %s"% (150,nome, bcolors.BOLD + "Status:" + bcolors.OKBLUE + " Disponível" + bcolors.ENDC))
            encontrado = Thread(target = tocarSom())
            encontrado.run
            tocarSom()
            if encontrado.is_alive:
                continue
