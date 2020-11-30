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
LOGGER.setLevel(logging.WARNING)


sites = ['google.com', 'www.kabum.com.br/cgi-local/site/listagem/listagem.cgi?string=Rx+6800+16G&btnG=',
    'www.pichau.com.br/hardware/placa-de-video?rgpu=6336%2C6337',
    'www.terabyteshop.com.br/busca?str=rx+6800+16GB']


def iniciar():
    options = uc.ChromeOptions()
    options.headless=True
    options.add_argument('--headless')
    chrome = uc.Chrome(options=options)
    return chrome

driver = iniciar()
for site in itertools.cycle(sites):
    adrs = "https://" + str(site)
    driver.get(adrs)
    if "kabum" in adrs:
        time.sleep(7)
        try:
            procurarProdutosKabum(driver)
        except(TimeoutException):
            print('erro Kabuuuuuuuuuuum')
            driver.close
    if "pichau" in adrs:
        time.sleep(7)
        try:
            procurarProdutosPichau(driver)
        except(TimeoutException):
            print('erro na pichaaaaaaaaaaaaaaaaaaaaaaaaaaau')
            driver.close
    if "terabyteshop" in adrs:
        time.sleep(7)
        try:
            procurarProdutosTera(driver)
        except(TimeoutException):
            print('erro na Terabyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyte')
            driver.close
    snap = site.split('.')[0]
    driver.save_screenshot(snap +'.png')


driver.quit()
