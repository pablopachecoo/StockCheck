from selenium.webdriver.common.by import By
from playsound import playsound
from Metodos.metodos import *
import babel.numbers


def procurarProdutosKabum(driver, limite):  

    cls()
    #print("%-*s    %s"% (58, '🌐   Kabum   🌐'))
    print("%-*s    %s"% (52, '', '🌐   Kabum   🌐 \n' ) + '', )
    
    #listaProdutos = driver.find_elements_by_css_selector('div.sc-HzFiz.jZYkIK.productCard') #Encontra os cards dos Produtos 
    listaProdutos = driver.find_elements_by_css_selector('div.sc-ff8a9791-7.dZlrn.productCard')
    
    
    #Lista dos Produtos
    disponiveis = []
    indisponiveis = []

    for p in listaProdutos:
        #sc-kIKDeO JmyVF sc-fIavCj ehdVvu nameCard
        nomeProduto = p.find_element(By.CSS_SELECTOR, 'span.sc-d99ca57-0.iRparH.sc-ff8a9791-16.kRYNji.nameCard').text #Encontra os card do Nome
        nomeProduto = nomeProduto.split(',', 1)[0]
        #Tenta ver se o texto do preço existe, e entra pra lista de Disponiveis se estiver dentro do valor limite.
        try:
            #pegando o texto do preco e tirando espaços '  '
            precoProduto = formatar(p.find_element(By.CSS_SELECTOR, 'span.sc-3b515ca1-2.jTvomc.priceCard').text)
            #formatando o precoProduto pra R$
            precoProdutoBrl = str(babel.numbers.format_currency(precoProduto, 'BRL'))

            #O Status também tem o valor do produto.
            status = precoProdutoBrl + " > Limit" if precoProduto > limite else precoProdutoBrl + " Disponivel" 
            disponiveis.append(p) if precoProduto < limite else None

            #a cor do output muda se o preço for maior que o limite
            corDoStatus = bcolors.WARNING if precoProduto > limite else bcolors.OKBLUE
            print(bcolors.BOLD + bcolors.OKCYAN + "Modelo:" + bcolors.ENDC + "%-*s    %s"% (85,nomeProduto, bcolors.BOLD + "Status:" + corDoStatus + status + bcolors.ENDC))

        except:
            print(bcolors.BOLD + "Modelo:" + bcolors.ENDC + "%-*s    %s"% (85,nomeProduto, bcolors.BOLD + "Status:" + bcolors.FAIL + "INDISPONIVEL"+ bcolors.ENDC))
            indisponiveis.append(p)
        
    print("Existem ", len(disponiveis), " produtos disponíveis.")
    return(disponiveis)
    