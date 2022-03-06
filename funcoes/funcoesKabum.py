from __future__ import print_function

from logging import log

from selenium.common.exceptions import NoSuchElementException, StaleElementReferenceException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from playsound import playsound
from Metodos.metodos import *
from threading import Thread
import babel.numbers
import decimal

#lista dos produtos
produtos = []

ts = []
listaDosProdutos = 0
indisponiveis=[]
disponiveis=[]

def compararPrecos():
    print('preco')

def procurarProdutosKabum(driver, limite):  

    pegarPreco = 3
    ignored_exceptions=(NoSuchElementException,StaleElementReferenceException,)

    listaProdutos = driver.find_elements_by_css_selector('div.sc-GEbAx.odTaK.productCard') #Encontra os cards dos Produtos
    login = WebDriverWait(driver, 10,ignored_exceptions=ignored_exceptions).until(EC.presence_of_element_located((By.XPATH, """.//*[@id="listing"]/article/section/div[2]/div/main""")))
    login = driver.find_elements(By.XPATH, """.//*[@id="listing"]/article/section/div[2]/div/main""")
    cls()
    print('****************************************************************************************Kabum*******************************************************************************************')

    def playy():
        playsound('alert.mp3', block = False)

    #produtos = []
    ts = []
    disponiveis = []
    precos = []

    # for x in listaProdutos:
    #     if x.get_attribute("class") == 'sc-GEbAx odTaK productCard':
    #         produtos.append(x)
    

    for p in listaProdutos:
        nomeProduto = p.find_element(By.CSS_SELECTOR, 'h2.sc-kHOZwM.brabbc.sc-fHeRUh.jwXwUJ.nameCard').text #Encontra os card do Nome

        try:
            #Se o texto do preço existe, entra pra lista de Disponiveis.
            precoProduto = p.find_element(By.CSS_SELECTOR, 'span.sc-iNGGcK.fTkZBN.priceCard').text
            disponiveis.append(p)
            print(bcolors.BOLD + "Modelo:" + bcolors.ENDC + "%-*s    %s"% (150,nomeProduto, bcolors.BOLD + "Status:" + bcolors.OKBLUE + "DISPONIVEL"+ bcolors.ENDC))

        except:
            print(bcolors.BOLD + "Modelo:" + bcolors.ENDC + "%-*s    %s"% (150,nomeProduto, bcolors.BOLD + "Status:" + bcolors.WARNING + "INDISPONIVEL"+ bcolors.ENDC))
            indisponiveis.append(p)
            listaProdutos.remove(p)

        if formatar(precoProduto) > limite:
            listaProdutos.remove(p)

        
    print("Temos ", len(disponiveis), " produtos disponíveis.")
    return(disponiveis)
    