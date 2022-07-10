import itertools

def run():
    '''
    Reto 77: Utiliza itertools para obtener los multiplos de 5
    de la siguiente lista. Imprime el resultado en una lista
    '''
    num_list = [1, 5, 10, 23, 3, 555, 11, 10]

    mult_list = itertools.filterfalse(lambda x : x % 5 != 0, num_list)
    print(list(mult_list))

if __name__ == '__main__':
    run()