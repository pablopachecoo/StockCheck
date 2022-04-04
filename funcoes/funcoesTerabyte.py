from logging import log
from multiprocessing.connection import wait
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
    

# def enterSite():
#     url = ''
#     DRIVER_PATH = 'chromedriver.exe'
#     options = Options()
#     driver = webdriver.Chrome(options=options, executable_path=DRIVER_PATH)
#     options.add_argument("--window-size=1920,1200")
#     driver.get(url)
#     return driver

def procurarProdutosTera(driver, limite):
   
    # try:
    #     produtos = WebDriverWait(driver, 10).until(EC.presence_of_all_elements_located((By.CSS_SELECTOR, 'pbox.col-xs-12.col-sm-6.col-md-3')))    #pegar o nome e o preço e ver se tem RX 6800 na string
    # except:
    #     ''

    # try:
    #     produtos = WebDriverWait(driver, 10).until(EC.presence_of_all_elements_located((By.CSS_SELECTOR, 'div.pbox.col-xs-12.col-sm-6.col-md-3')))    #pegar o nome e o preço e ver se tem RX 6800 na string
    # except:
    #     ''
        

    # try:
    #     produtos = WebDriverWait(driver, 10).until(EC.presence_of_all_elements_located((By.CSS_SELECTOR, 'pbox.col-xs-12.col-sm-6.col-md-3')))    #pegar o nome e o preço e ver se tem RX 6800 na string
    # except:
    #     ''

    try:
        produtos = WebDriverWait(driver, 25).until(EC.presence_of_all_elements_located((By.CSS_SELECTOR, 'div.commerce_columns_item_inner')))    #pegar o nome e o preço e ver se tem RX 6800 na string
        # produtos = driver.find_elements_by_css_selector('div.commerce_columns_item_inner')
        # driver.save_screenshot('screenie.png')
    except:
        driver.save_screenshot('screenie.png')

    cls()
    print('****************************************************************************************Terabyte Shop***************************************************************************************')

    ignored_exceptions=(NoSuchElementException,StaleElementReferenceException,)
    atual = 1
    for p in produtos: #//*[@id="prodarea"]/div[1]/div/div[4]

        preco = driver.find_elements_by_xpath("""//*[@id="prodarea"]/div["""+str(atual)+"""]/div/div[4]/div[1]/div[2]/span""")
        precoTexto = preco[0].text
        precoTexto = formatar(precoTexto)

        try:
            #depois do R$ tira tudo inutil
            sep = '\nR$'
            # nome = p.find_element_by_xpath("""//*[@id="prodarea"]/div["""+str(produtos.index(p)+1)+"""]/div/div[3]/a/h2/strong""").text
            nome = p.text
            stripped = nome.split(sep, 1)[0]

        except:
            continue
                
        #nome = p.find_element_by_xpath()
        if 'vendidos' in nome:
            if int(float(precoTexto)) <= limite:
                
                print(bcolors.BOLD + "Modelo:" + bcolors.ENDC + "%-*s    %s"% (150,nome, bcolors.BOLD + "Status:" + bcolors.FAIL + " Indisponível |" + bcolors.ENDC))
                          
            # indisponivel  print(bcolors.BOLD + "Modelo:" + bcolors.ENDC + "%-*s    %s"% (150,nome, bcolors.BOLD + "Status:" + bcolors.FAIL + " Indisponível" + bcolors.ENDC))
        if "PC" in nome:
            continue
        else:
            if int(float(precoTexto)) <= limite:
                print (bcolors.BOLD + "Modelo:" + bcolors.ENDC + "%-*s    %s"% (150,nome, bcolors.BOLD + "Status:" + bcolors.OKBLUE + " Disponível |" + bcolors.ENDC))
            else:
                print(bcolors.BOLD + "Modelo:" + bcolors.ENDC + "%-*s    %s"% (150,nome, bcolors.BOLD + "Status:" + bcolors.WARNING + " TAKARO ™ |" + bcolors.ENDC))  

        atual+1

