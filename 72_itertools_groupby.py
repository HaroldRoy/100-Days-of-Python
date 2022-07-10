import itertools

def run():
    '''
    Reto 72: Utiliza itertools para obtener la cantidad
    de veces que se repite cada número en la lista. Imprime
    el resultado en un diccionario con el formato
    {numero: cantidad de repeticiones}
    '''
    num_list = [0, 1, 1, 2, 3, 2, 4, 5, 5, 8, 4]
    
    rep_list = {k: len(list(i)) for k, i in itertools.groupby(sorted(num_list))}
    print(rep_list)


if __name__ == '__main__':
    run()