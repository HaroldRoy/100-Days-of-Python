def run():
    '''
    Reto 56: Utiliza una funcion lambda para encontrar
    la raiz cuadrada de esta lista de numeros [49, 4, 36, 16, 25]
    Imprime el resultado en una nueva lista
    '''
    num_list = [49, 4, 36, 16, 25]
    
    root = lambda x: x**(1/2)
    square_list = [root(x) for x in num_list]
    print(square_list)
    
if __name__ == '__main__':
    run()