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
from selenium import webdriver

LOGGER.setLevel(logging.WARNING)

vari = 1

def bypass(var):
    if (var % 2) == 0:
        return ''
    else:
        return '+'

sites = ['www.kabum.com.br/cgi-local/site/listagem/listagem.cgi?string=Rx+6800+16G+&btnG=',
    'www.pichau.com.br/hardware/placa-de-video?rgpu=6336%2C6337',
    'www.terabyteshop.com.br/busca?str=rx+6800+16GB']


def iniciar():
    options = webdriver.ChromeOptions()
    driver = webdriver.Chrome('chromedriver')
    options.headless = True
    options.add_argument(f"--window-size=1920,1080")
    options.add_argument("--hide-scrollbars")
    options.add_argument("--log-level=3")
    options.add_argument('--disable-extensions')
    options.add_argument('--profile-directory=Default')
    options.add_argument("--incognito")
    options.add_argument("--disable-plugins-discovery");
    driver = uc.Chrome(options=options)
    #chrome.delete_all_cookies()
    return driver

driver = iniciar()
for site in itertools.cycle(sites):
    adrs = "https://" + str(site)
    print()
    #wait = randrange(20,110)
    if "kabum" in adrs:
        driver.get(adrs)
        #time.sleep(wait)
        try:
            procurarProdutosKabum(driver)
        except(TimeoutException):
            print('erro Kabum')
            driver.save_screenshot('errokabum.png')
            driver.close
    if "pichau" in adrs:
        driver.get(adrs)
        #time.sleep(wait)
        try:
            procurarProdutosPichau(driver)
        except(TimeoutException):
            print('erro na Pichau')
            driver.save_screenshot('erropichau.png')
            time.sleep(1)
    if "terabyteshop" in adrs:
        driver.get(adrs)
        #time.sleep(wait)
        try:
            procurarProdutosTera(driver)
        except(TimeoutException):
            print('erro na Terabyte')
            driver.save_screenshot('erroterabyte.png')
            driver.close
    vari += 1
driver.quit()
