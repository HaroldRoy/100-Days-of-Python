import re

def run():
    '''
    Reto 61: Utiliza Regex para validar que las cadenas de la
    lista sean totalmente numericas. Imprime una lista con las
    cadenas numericas.
    '''
    char_list = ["20200806", "jun122022", "202204DD", "20221208", "22mar2022"]
    
    num_list = [element for element in char_list if re.match('^[0-9]*$', element)]
    print(num_list)

    # correos = ["20200806", "jun122022", "202204DD", "20221208", "22mar2022"]
    # patron = '[\d]{8}'
    # validos = [c for c in correos if re.search(patron, c)]
    # print(validos)


if __name__ == '__main__':
    run()