import itertools

def run():
    '''
    Reto 80: Utiliza itertools para repetir el numero 80
    5 veces en una lista. Imprime el resultado en una lista
    '''
    num_list = list(itertools.repeat(80, 5))
    print(num_list)
    

if __name__ == '__main__':
    run()