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

produtos = []
ts = []
listadosProdutos = 0
disponiveis=[]

def compararPrecos():
    print('preco')

def procurarProdutosKabum(driver, limite):  
    firstProduto = 3
    pegarPreco = 3
    ignored_exceptions=(NoSuchElementException,StaleElementReferenceException,)


    login = WebDriverWait(driver, 10,ignored_exceptions=ignored_exceptions).until(EC.presence_of_element_located((By.XPATH, """.//*[@id="listing"]/article/section/div[2]/div/main""")))
    login = driver.find_elements(By.XPATH, """.//*[@id="listing"]/article/section/div[2]/div/main""")
    cls()
    print('****************************************************************************************Kabum*******************************************************************************************')

    def playy():
        playsound('alert.mp3', block = False)

    produtos = []
    ts = []
    disponiveis = []
    precos = []

    for x in login:
        if x.get_attribute("class") == 'sc-GEbAx odTaK productCard':
            produtos.append(x)
    

    for p in produtos:
        xpathPreco = """//*[@id="listagem-produtos"]/div/div["""+ str(firstProduto) + """]/div/div[2]/div[1]/div["""+ str(pegarPreco) + """]"""
        talvezPreco = WebDriverWait(driver, 10,ignored_exceptions=ignored_exceptions).until(EC.presence_of_all_elements_located((By.XPATH, xpathPreco)))
        tamanhofonte = talvezPreco[0].value_of_css_property("font-size")
        if tamanhofonte == '21px': #Se o tamanho da fonte for a do Preço

            #Vou refatorar isso, eu juro.
            a = talvezPreco[0].text.replace('R$', '')
            b = a.replace(' ', '')
            c = b.replace('.',' ')
            d = c.replace(',','.')
            b = d.replace(' ', '')
            currency = "{:,.2f}".format(int(float(b)))
            a = str(currency)
            b = a.replace(',', '.')
            b = a.replace(',', '')
            #print(b)
            precos.append(b) ##aquiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiii


        if tamanhofonte == '10px': #Se o tamanho da fonte for a do "Em até 12x sem juros" (pegando +1 div depois)
            pegarPreco = 4
            xpathPreco = """//*[@id="listagem-produtos"]/div/div["""+ str(firstProduto) + """]/div/div[2]/div[1]/div["""+ str(pegarPreco) + """]"""
            talvezPreco = WebDriverWait(driver, 10,ignored_exceptions=ignored_exceptions).until(EC.presence_of_all_elements_located((By.XPATH, xpathPreco)))
            a = talvezPreco[0].text.replace('R$', '')
            b = a.replace(' ', '')
            c = b.replace('.',' ')
            d = c.replace(',','.')
            b = d.replace(' ', '')
            
            currency = "{:,.2f}".format(int(float(b)))
            #print(currency)
            a = str(currency)
            #print(a)
            b = a.replace(',', '.')
            b = a.replace(',', '')
            #print(b)
            precos.append(b)


        xpath = """//*[@id="listagem-produtos"]/div/div["""+ str(firstProduto) + """]/div"""
        ts.append(p.find_elements_by_xpath(xpath))
        pegarPreco = 3
        firstProduto += 1


    #sc-fznWqX qatGF ---- *CLASS DO PRECO*
    firstProduto = 3
    indexValores = 0
    for x in ts:
        xpath2 = """//*[@id="listagem-produtos"]/div/div["""+ str(firstProduto) + """]/div/div[2]/div[2]/div"""
        xnomePlaca = """//*[@id="listagem-produtos"]/div/div["""+ str(firstProduto) + """]/div/div[1]/a"""
        nomePlaca= WebDriverWait(driver, 10,ignored_exceptions=ignored_exceptions).until(EC.presence_of_all_elements_located((By.XPATH, xnomePlaca))) #botao comprar
        a = x[0]
        c = WebDriverWait(driver, 10,ignored_exceptions=ignored_exceptions).until(EC.presence_of_all_elements_located((By.XPATH, xpath2))) #botao comprar
        imagem = c[0].find_element_by_xpath("""//*[@id="listagem-produtos"]/div/div["""+ str(firstProduto) + """]/div/div[2]/div[2]/div/img""")
        disponivel = imagem.get_attribute("src")

        if disponivel == 'https://static.kabum.com.br/conteudo/temas/001/imagens/icones/comprar.png':
            if int(float(precos[indexValores])) <= limite:
                disponiveis.append(ts[indexValores])
                
                print(bcolors.BOLD + "Modelo:" + bcolors.ENDC + "%-*s    %s"% (150,nomePlaca[0].text, bcolors.BOLD + "Status:" + bcolors.OKBLUE + "    | DISPONÍVEL " + bcolors.ENDC))
                #playsound('alert.mp3') #se tocar o som pela função toca 2x
            else:
                print(bcolors.BOLD + "Modelo:" + bcolors.ENDC + "%-*s    %s"% (150,nomePlaca[0].text, bcolors.BOLD + "Status:" + bcolors.WARNING + babel.numbers.format_currency(precos[indexValores], 'BRL') + '    | TAKARO ™ ' + bcolors.ENDC))
        else:
            print (bcolors.BOLD + "Modelo:" + bcolors.ENDC + "%-*s    %s"% (150,nomePlaca[0].text, bcolors.BOLD + "Status:" + bcolors.FAIL + babel.numbers.format_currency(precos[indexValores], 'BRL') + '    | ESGOTADO ' + bcolors.ENDC))

        firstProduto += 1
        indexValores += 1
    print("Temos ", len(disponiveis), " produtos que atendem a esses requisitos")
    return(disponiveis)
    