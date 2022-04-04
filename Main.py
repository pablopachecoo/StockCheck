from selenium.common.exceptions import TimeoutException
from funcoes.funcoesKabum import procurarProdutosKabum
from funcoes.funcoesPichau import procurarProdutosPichau
from funcoes.funcoesTerabyte import procurarProdutosTera
import time
from logging import log
import itertools
import undetected_chromedriver as uc
import logging
from selenium.webdriver.remote.remote_connection import LOGGER
from random import randrange
import decimal
from selenium import webdriver

LOGGER.setLevel(logging.WARNING)

limite = float(300.00)


sites = ['www.kabum.com.br/busca?query=oooi',
     'www.pichau.com.br/hardware/placa-de-video?rgpu=6347',
     'www.terabyteshop.com.br/busca?str=RX+6900+16GB']

#sites = [     'www.pichau.com.br/hardware/placa-de-video?rgpu=6347', 'www.terabyteshop.com.br/busca?str=RX+6900+16GB']


def iniciar():
    crome_options = uc.ChromeOptions()
    #crome_options.add_argument('--headless')
    crome_options.add_argument('--disable-blink-features=AutomationControlled')
    crome_options.add_argument("--disable-plugins-discovery")
    crome_options.add_argument('--disable-extensions')
    crome_options.add_argument(f"--window-size=1920,1080")
    crome_options.add_argument("--hide-scrollbars")
    crome_options.add_argument("--log-level=3")
    crome_options.add_argument('--profile-directory=Default')
    crome_options.add_argument("--incognito")
    crome_options.add_argument("start-maximized")
    crome_options.add_experimental_option("excludeSwitches", ["enable-automation"])
    crome_options.add_experimental_option('useAutomationExtension', False)
    #tem tudo isso de options para evitar a detecção, especialmente pela terabyte.
    driver = webdriver.Chrome(executable_path=r'./chromedriver.exe', options=crome_options)
    #chrome.delete_all_cookies()
    return driver


driver = iniciar()

#mais um comando pra evitar detecção
driver.execute_cdp_cmd('Network.setUserAgentOverride', {"userAgent": 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.53 Safari/537.36'})

#Itertools é um loop Eterno dentro da lista dos Sites ∞
for site in itertools.cycle(sites):
    adrs = "https://" + str(site)

    if "kabum" in adrs:
        #Esse wait serve pra deixar um tempo de request aleatório entre X e Y segundos
        wait = randrange(15,30)
        driver.get(adrs)
        #time.sleep(wait)
        try:
            procurarProdutosKabum(driver, limite)
        except(TimeoutException):
            print('erro Kabum')
            #driver.save_screenshot('errokabum.png')
            driver.close

    if "pichau" in adrs:
        driver.get(adrs)
        #time.sleep(wait)
        try:
            procurarProdutosPichau(driver, limite)
        except(TimeoutException):
            print('Erro na Pichau')
            #driver.save_screenshot('erropichau.png')
            time.sleep(1)

    if "terabyteshop" in adrs:
        wait = randrange(15,30)
        driver.get(adrs)
        #time.sleep(wait)
        try:
            procurarProdutosTera(driver, limite)
        except(TimeoutException):
            print('erro na Terabyte')
            #driver.save_screenshot('erroterabyte.png')
            driver.close
driver.quit()
