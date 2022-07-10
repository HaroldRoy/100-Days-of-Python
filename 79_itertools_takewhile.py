import itertools

def run():
    '''
    Reto 79: Utiliza itertools para obtener los elementos
    de la siguiente lista hasta que alguno contenga un "0".
    Imprime el resultado en una lista
    '''
    num_list = [2, 3, 5, 7, 13, 103, 25, 15, 45]
    
    filter_list = itertools.takewhile(lambda x : '0' not in str(x), num_list)
    print(list(filter_list))


if __name__ == '__main__':
    run()