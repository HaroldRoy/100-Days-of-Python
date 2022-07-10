import re

def run():
    '''
    Reto 65: Utiliza Regex para quitar los prefijos telefonicos
    de los telefonos de la lista. Imprime una lista con los
    telefonos sin prefijos telefonicos 
    '''
    phone_list = [
        '+54 11 1234 5678',
        '+591 68754321',
        '+56 9 8765 4321',
        ]

    only_phone = [re.sub('^\+?(\d+)\s', '', p) for p in phone_list]
    print(only_phone)


if __name__ == '__main__':
    run()