import os
from logging import log
import time
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException, StaleElementReferenceException
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support import wait
import os
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from playsound import playsound

class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'



produtos = []
ts = []
listadosProdutos = 0
disponiveis=[]

def cls():
    os.system('cls' if os.name=='nt' else 'clear')

#https://www.pichau.com.br/hardware/placa-de-video?rgpu=6336%2C6337
def procurarProdutosKabum(driver):
    ignored_exceptions=(NoSuchElementException,StaleElementReferenceException,)
    login = WebDriverWait(driver, 10,ignored_exceptions=ignored_exceptions).until(expected_conditions.presence_of_all_elements_located((By.XPATH, """//*[@id="listagem-produtos"]/div/div""")))
    #login = driver.find_elements_by_xpath("""//*[@id="listagem-produtos"]/div/div""")    #pegar o nome e o preço e ver se tem RX 6800 na string
    cls()
    print('****************************************************************************************KABUM*******************************************************************************************')
    inicio = 1
    
    produtos = []
    ts = []
    disponiveis = []
    for x in login:
        if x.get_attribute("class") == 'sc-fzqARJ eITELq':
            produtos.append(x)
    firstProduto = 3

    for p in produtos:
        xpath = """//*[@id="listagem-produtos"]/div/div["""+ str(firstProduto) + """]/div"""
        ts.append(p.find_elements_by_xpath(xpath))
        firstProduto += 1
    firstProduto = 3
    
    for x in ts:
        xpath2 = """//*[@id="listagem-produtos"]/div/div["""+ str(firstProduto) + """]/div/div[2]/div[2]/div"""
        xnomePlaca = """//*[@id="listagem-produtos"]/div/div["""+ str(firstProduto) + """]/div/div[1]/a"""
        nomePlaca= WebDriverWait(driver, 10,ignored_exceptions=ignored_exceptions).until(expected_conditions.presence_of_all_elements_located((By.XPATH, xnomePlaca))) #botao comprar
        a = x[0]
        c = WebDriverWait(driver, 10,ignored_exceptions=ignored_exceptions).until(expected_conditions.presence_of_all_elements_located((By.XPATH, xpath2))) #botao comprar
        imagem = c[0].find_element_by_xpath("""//*[@id="listagem-produtos"]/div/div["""+ str(firstProduto) + """]/div/div[2]/div[2]/div/img""")
        compravel = imagem.get_attribute("src")
        if compravel == 'https://static.kabum.com.br/conteudo/temas/001/imagens/icones/comprar.png':
            disponiveis.append(a)
            print(nomePlaca[0].text, ' KABUM Disponivel')
            playsound('C:/Users/power/bot/trem.wav')
        else:
            #print(nomePlaca[0].text, '%50s' %  ' | KABUM Indisponível')
            #bcolors.WARNING + "Status" + bcolors.ENDC
            print (bcolors.FAIL + "Modelo:" + bcolors.ENDC +  "%-*s   Status: %s" % (150,nomePlaca[0].text,bcolors.FAIL + " Indisponível" + bcolors.ENDC))
        firstProduto += 1
    print("Temos ", len(disponiveis), " produtos que atendem a esses requisitos")