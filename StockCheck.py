from selenium.common.exceptions import TimeoutException
from funcoes.funcoesKabum import procurarProdutosKabum
from funcoes.funcoesPichau import procurarProdutosPichau
from funcoes.funcoesTerabyte import procurarProdutosTera
import time
from logging import log
import itertools
import undetected_chromedriver.v2 as uc
import logging
from selenium.webdriver.remote.remote_connection import LOGGER
from random import randrange
from selenium import webdriver
import decimal

LOGGER.setLevel(logging.WARNING)

limite = decimal.Decimal(13500.00)

sites = ['www.kabum.com.br/cgi-local/site/listagem/listagem.cgi?string=Rx+6900+16G&btnG=',
    
    'www.terabyteshop.com.br/busca?str=RX+6900+16GB']


def iniciar():
    crome_options = uc.ChromeOptions()
    #crome_options.add_argument('--headless')
    crome_options.add_argument(f"--window-size=1920,1080")
    crome_options.add_argument("--hide-scrollbars")
    crome_options.add_argument("--log-level=3")
    crome_options.add_argument('--disable-extensions')
    crome_options.add_argument('--profile-directory=Default')
    crome_options.add_argument("--incognito")
    crome_options.add_argument("--disable-plugins-discovery");
    #crome_options.add_argument('--headless')
    #driver = webdriver.Chrome(r'C:/Users/power/Documents/Projecttos/Stock Check py/chromedriver', options=crome_options)
    driver = uc.Chrome(options=crome_options)
    #chrome.delete_all_cookies()
    return driver


driver = iniciar()
for site in itertools.cycle(sites):
    adrs = "https://" + str(site)
    print()
    
    if "kabum" in adrs:
        wait = randrange(15,30)
        driver.get(adrs)
        time.sleep(wait)
        try:
            procurarProdutosKabum(driver, limite)
        except(TimeoutException):
            print('erro Kabum')
            driver.save_screenshot('errokabum.png')
            driver.close

    if "pichau" in adrs:
        wait = randrange(15,30)
        driver.get(adrs)
        #time.sleep(wait)
        try:
            procurarProdutosPichau(driver, limite)
        except(TimeoutException):
            print('Erro na Pichau')
            driver.save_screenshot('erropichau.png')
            time.sleep(1)

    if "terabyteshop" in adrs:
        wait = randrange(15,30)
        driver.get(adrs)
        #time.sleep(wait)
        try:
            procurarProdutosTera(driver, limite)
        except(TimeoutException):
            print('erro na Terabyte')
            driver.save_screenshot('erroterabyte.png')
            driver.close
driver.quit()
