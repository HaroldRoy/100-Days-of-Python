import re

def run():
    '''
    Reto 64: Utiliza Regex para quitar los ceros innecesarios
    de las direcciones IP de la lista. Imprime una lista
    con las IP validas 
    '''
    ip_list = [
        '192.08.001.5',
        '10.120.023.001',
        '192.160.2.1',
        ]

    ip_correct = [re.sub('\.[0]*', '.', e) for e in ip_list]
    print(ip_correct)


if __name__ == '__main__':
    run()