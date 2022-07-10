import itertools

def run():
    '''
    Reto 76: Utiliza itertools para obtener el valor maximo
    de cada tupla de la siguiente lista. Imprime el resultado
    en una lista
    '''
    num_list = [(2, 4, 6), (7, 8, 5, 6), (5, 10)]

    max_list = list(itertools.starmap(max, num_list))
    print(max_list)


if __name__ == '__main__':
    run()