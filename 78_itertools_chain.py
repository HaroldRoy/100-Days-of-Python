import itertools

def run():
    '''
    Reto 78: Utiliza itertools para unir las siguientes tuplas.
    Obtiene el tipo de cada dato e imprimelo en una lista.
    '''
    tuple_1, tuple_2 = (78, 100), ('Dias', 'Python')
    
    join_tuples = [type(elem) for elem in itertools.chain(tuple_1, tuple_2)]
    print(join_tuples)


if __name__ == '__main__':
    run()