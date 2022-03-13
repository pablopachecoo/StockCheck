from selenium.webdriver.common.by import By
from playsound import playsound
from Metodos.metodos import *
import babel.numbers


def procurarProdutosKabum(driver, limite):  

    cls()
    print('****************************************************************************************Kabum*******************************************************************************************')
    listaProdutos = driver.find_elements_by_css_selector('div.sc-GEbAx.odTaK.productCard') #Encontra os cards dos Produtos
                                                              #sc-GEbAx.odTaK.productCard
    #Lista dos Produtos
    disponiveis = []
    indisponiveis = []

    for p in listaProdutos:
        nomeProduto = p.find_element(By.CSS_SELECTOR, 'h2.sc-kHOZwM.brabbc.sc-fHeRUh.jwXwUJ.nameCard').text #Encontra os card do Nome

        #Tenta ver se o texto do preço existe, e entra pra lista de Disponiveis se estiver dentro do valor limite.
        try:
            #pegando o texto do preco e tirando espaços '  '
            precoProduto = formatar(p.find_element(By.CSS_SELECTOR, 'span.sc-iNGGcK.fTkZBN.priceCard').text)
            #formatando o precoProduto pra R$
            precoProdutoBrl = str(babel.numbers.format_currency(precoProduto, 'BRL'))

            #O Status também tem o valor do produto.
            status = precoProdutoBrl + " > Limite" if precoProduto > limite else precoProdutoBrl + " Disponivel" 
            disponiveis.append(p) if precoProduto < limite else None

            #a cor do output muda se o preço for maior que o limite
            corDoStatus = bcolors.WARNING if precoProduto > limite else bcolors.OKBLUE
            print(bcolors.BOLD + "Modelo:" + bcolors.ENDC + "%-*s    %s"% (150,nomeProduto, bcolors.BOLD + "Status:" + corDoStatus + status + bcolors.ENDC))

        except:
            print(bcolors.BOLD + "Modelo:" + bcolors.ENDC + "%-*s    %s"% (150,nomeProduto, bcolors.BOLD + "Status:" + bcolors.FAIL + "INDISPONIVEL"+ bcolors.ENDC))
            indisponiveis.append(p)
        
    print("Existem ", len(disponiveis), " produtos disponíveis.")
    return(disponiveis)
    