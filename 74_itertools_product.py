import itertools

def run():
    '''
    Reto 74: Utiliza itertools para obtener el producto
    cartesiano de las siguientes listas. Imprime el resultado
    en una lista de tuplas
    '''
    a_list = [1, 3, 5]
    b_list = [2, 4, 6]
    
    join_list = [a_list, b_list]
    resultado = list(itertools.product(*join_list))
    print(resultado)


if __name__ == '__main__':
    run()