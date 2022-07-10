import itertools

def run():
    '''
    Reto 71: Utiliza itertools para generar una serie
    de sumas acumuladas con los números de la siguiente
    lista. Imprime el resultado 
    '''
    num_list = [0, 1, 1, 2, 3, 5, 8]

    sum_list = list(itertools.accumulate(num_list))
    print(sum_list)


if __name__ == '__main__':
    run()