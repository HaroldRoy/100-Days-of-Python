import itertools

def run():
    '''
    Reto 73: Utiliza itertools para obtener todas las
    permutaciones posibles con las letras de la siguiente
    lista. Imprime el resultado en una lista de tuplas
    '''
    my_list = ["r", "i", "o"]
    
    permut = itertools.permutations(my_list)
    list_permut = [p for p in list(permut)]
    print(list_permut)


if __name__ == '__main__':
    run()