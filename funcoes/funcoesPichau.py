from logging import log
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException, StaleElementReferenceException
from funcoes.prints import capturar 
from playsound import playsound
from Metodos.metodos import *



def procurarProdutosPichau(driver):
    produtos = []
    disponiveis=[]
    login = driver.find_elements_by_xpath("""//*[@id="amasty-shopby-product-list"]/div[2]/ol/li""")    #pegar o nome e o preço e ver se tem RX 6800 na string
    cls()
    print('****************************************************************************************Pichau***************************************************************************************')
    for x in login:
        if x.get_attribute("class") == 'item product product-item':
            #print(x.text)
            produtos.append(x)
        else:
            print('**div não é um produto**')

    ignored_exceptions=(NoSuchElementException,StaleElementReferenceException,)
    for p in produtos:
        ordem = produtos.index(p)+1
        ximagemAnuncio = """//*[@id="amasty-shopby-product-list"]/div[2]/ol/li[""" + str(produtos.index(p)+1) + """]"""
        xnomePlaca = """//*[@id="amasty-shopby-product-list"]/div[2]/ol/li[""" + str(produtos.index(p)+1) + """]/div/div/strong/a"""
        nome = WebDriverWait(driver, 10,ignored_exceptions=ignored_exceptions).until(EC.presence_of_element_located((By.XPATH, xnomePlaca))) #botao comprar
        foto = WebDriverWait(driver, 10,ignored_exceptions=ignored_exceptions).until(EC.presence_of_element_located((By.XPATH, ximagemAnuncio))) #imagem da placa
        if "PRODUTO INDISPONÍVEL" in p.text:
            print(bcolors.BOLD + "Modelo:" + bcolors.ENDC + "%-*s    %s"% (150,nome.text, bcolors.BOLD + "Status:" + bcolors.FAIL + " Indisponível" + bcolors.ENDC))
        else:
            capturar(driver, foto, ordem)
            print(bcolors.BOLD + "Modelo:" + bcolors.ENDC + "%-*s    %s"% (150,nome.text, bcolors.BOLD + "Status:" + bcolors.OKBLUE + " DISPONÍVEL !" + bcolors.ENDC))
            disponiveis.append(p)
            playsound('alert.mp3')
    print("Temos ", len(disponiveis), " produtos que atendem a esses requisitos")