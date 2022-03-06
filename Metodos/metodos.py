import os

def cls():
    os.system('cls' if os.name=='nt' else 'clear')

class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'


#Remove "R$" e espaços em branco
def formatar(precoTexto):
    precoTexto = precoTexto.replace('.','')
    precoTexto = precoTexto.replace(',','.')
    precoTexto = precoTexto.replace(' ','')
    return float(precoTexto.replace('R$', ''))
