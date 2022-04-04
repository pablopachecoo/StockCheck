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

    disponiveis=[]
    cls()
    print('****************************************************************************************Pichau***************************************************************************************')

    produtos = WebDriverWait(driver, 10).until(EC.presence_of_all_elements_located((By.CSS_SELECTOR, 'div.MuiGrid-root.MuiGrid-item.MuiGrid-grid-xs-6.MuiGrid-grid-sm-6.MuiGrid-grid-md-4.MuiGrid-grid-lg-3.MuiGrid-grid-xl-2')))

    ignored_exceptions=(NoSuchElementException,StaleElementReferenceException,)
    for p in produtos:

        #pega o nome do produto e tirar caracteres desnecessários no final, o 'p.text' por si só, volta preço e outras coisas inúteis.
        nomeProduto = p.text.strip().split("\n",1)[0]

        if "Esgotado" in p.text:
            #print do nome do produto e "INDISPONÍVEL"
            print(bcolors.BOLD + "Modelo:" + bcolors.ENDC + "%-*s    %s"% (150,nomeProduto, bcolors.BOLD + "Status:" + bcolors.FAIL + " Indisponível" + bcolors.ENDC))
        else:
            #print do nome do produto e "DISPONÍVEL"
            #falta colocar o valor do produto no print
            print(bcolors.BOLD + "Modelo:" + bcolors.ENDC + "%-*s    %s"% (150,nomeProduto, bcolors.BOLD + "Status:" + bcolors.OKBLUE + " DISPONÍVEL !" + bcolors.ENDC))
            disponiveis.append(p)
    print("Temos ", len(disponiveis), " produtos disponíveis.")
    return(disponiveis)