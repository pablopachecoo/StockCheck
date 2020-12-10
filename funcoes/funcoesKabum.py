from logging import log
from selenium.common.exceptions import NoSuchElementException, StaleElementReferenceException
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from playsound import playsound
from Metodos.metodos import *


produtos = []
ts = []
listadosProdutos = 0
disponiveis=[]

def procurarProdutosKabum(driver):
    ignored_exceptions=(NoSuchElementException,StaleElementReferenceException,)
    login = WebDriverWait(driver, 10,ignored_exceptions=ignored_exceptions).until(EC.presence_of_all_elements_located((By.XPATH, """//*[@id="listagem-produtos"]/div/div""")))
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
        nomePlaca= WebDriverWait(driver, 10,ignored_exceptions=ignored_exceptions).until(EC.presence_of_all_elements_located((By.XPATH, xnomePlaca))) #botao comprar
        a = x[0]
        c = WebDriverWait(driver, 10,ignored_exceptions=ignored_exceptions).until(EC.presence_of_all_elements_located((By.XPATH, xpath2))) #botao comprar
        imagem = c[0].find_element_by_xpath("""//*[@id="listagem-produtos"]/div/div["""+ str(firstProduto) + """]/div/div[2]/div[2]/div/img""")
        disponivel = imagem.get_attribute("src")
        if disponivel == 'https://static.kabum.com.br/conteudo/temas/001/imagens/icones/comprar.png':
            disponiveis.append(a)
            print(bcolors.BOLD + "Modelo:" + bcolors.ENDC + "%-*s    %s"% (150,nomePlaca[0].text, bcolors.BOLD + "Status:" + bcolors.OKBLUE + " DISPONÍVEL !" + bcolors.ENDC))
            playsound('alert.mp3')
        else:       #bcolors.BOLD + "Modelo:" + bcolors.ENDC + "%-*s    %s"% (150,nomePlaca[0].text, bcolors.BOLD + "Status:" + bcolors.FAIL + " Indisponível" + bcolors.ENDC)
            print (bcolors.BOLD + "Modelo:" + bcolors.ENDC + "%-*s    %s"% (150,nomePlaca[0].text, bcolors.BOLD + "Status:" + bcolors.FAIL + " Indisponível" + bcolors.ENDC))
        firstProduto += 1
    print("Temos ", len(disponiveis), " produtos que atendem a esses requisitos")