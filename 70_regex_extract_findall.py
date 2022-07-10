import re

def run():
    '''
    Reto 70: Utiliza Regex para extraer todas las palabras
    que contengan al menos una 'a' en la siguiente cadena.
    Imprime una lista con las palabras extraidas
    '''
    txt = 'LLevas programando 70 dias seguidos'
    
    subchain = re.findall('[\w]*a[\w]*', txt)
    print(subchain)

if __name__ == '__main__':
    run()