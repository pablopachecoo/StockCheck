from cgitb import text
from logging import log
from operator import indexOf
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException, StaleElementReferenceException
#from funcoes.prints import capturar 
from playsound import playsound
from Metodos.metodos import *

#mais um dia de trabalho duro !

def procurarProdutosPichau(driver, limite):
    #//*[@id="__next"]/main/div[2]/div/div[1]/div[2]/div[1] --> Primeiro produtO
    #//*[@id="__next"]/main/div[2]/div/div[1]/div[2]/div[2]

    disponiveis=[]
    cls()
    print('****************************************************************************************Pichau***************************************************************************************')
    #produtos = driver.find_elements_by_css_selector('div.MuiGrid-root.MuiGrid-item.MuiGrid-grid-xs-12.MuiGrid-grid-sm-6.MuiGrid-grid-md-4.MuiGrid-grid-lg-3.MuiGrid-grid-xl-2')    #pegar o nome e o preço e ver se tem RX 6800 na string
    #produtos2 = driver.find_element_by_css_selector("div.MuiGrid-root.MuiGrid-item.MuiGrid-grid-xs-6.MuiGrid-grid-sm-6.MuiGrid-grid-md-4.MuiGrid-grid-lg-3.MuiGrid-grid-xl-2")
    produtos = WebDriverWait(driver, 10).until(EC.presence_of_all_elements_located((By.CSS_SELECTOR, 'div.MuiGrid-root.MuiGrid-item.MuiGrid-grid-xs-6.MuiGrid-grid-sm-6.MuiGrid-grid-md-4.MuiGrid-grid-lg-3.MuiGrid-grid-xl-2'))) #botao comprar
    #
    cls()
    print('****************************************************************************************Pichau***************************************************************************************')
    # for x in produtos:
    #     if x.get_attribute("class") == 'MuiGrid-root jss261 MuiGrid-container MuiGrid-spacing-xs-3':
    #         #print(x.text)
    #         produtos.append(x)
    #     else: 
    #         print('**div não é um produto**')

    ignored_exceptions=(NoSuchElementException,StaleElementReferenceException,)
    for p in produtos:
        #ordem = produtos.index(p)+1
        #ximagemAnuncio = """//*[@id="amasty-shopby-product-list"]/div[2]/ol/li[""" + str(produtos.index(p)+1) + """]"""

        #pega o nome do produto e tirar caracteres desnecessários no final, o p.text por si só,  volta preço e outras coisas inúteis.
        nomeProduto = p.text.strip().split("\n",1)[0]


        #nome = WebDriverWait(driver, 10,ignored_exceptions=ignored_exceptions).until(EC.presence_of_element_located((By.XPATH, xnomePlaca))) #botao comprar
        #foto = WebDriverWait(driver, 10,ignored_exceptions=ignored_exceptions).until(EC.presence_of_element_located((By.XPATH, ximagemAnuncio))) #imagem da placa
        if "Esgotado" in p.text:
            print(bcolors.BOLD + "Modelo:" + bcolors.ENDC + "%-*s    %s"% (150,nomeProduto, bcolors.BOLD + "Status:" + bcolors.FAIL + " Indisponível" + bcolors.ENDC))
        else:
            #capturar(driver, foto, ordem)
            print(bcolors.BOLD + "Modelo:" + bcolors.ENDC + "%-*s    %s"% (150,nomeProduto, bcolors.BOLD + "Status:" + bcolors.OKBLUE + " DISPONÍVEL !" + bcolors.ENDC))
            disponiveis.append(p)
            #playsound('alert.mp3')
        #playsound('alert.mp3')
    print("Temos ", len(disponiveis), " produtos disponíveis.")
    return(disponiveis)