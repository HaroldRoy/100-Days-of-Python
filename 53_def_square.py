def calculate_square(num_list: list):
    '''
    Funcion que eleva listas de numeros al cuadrado
    Args:
        num_list (list): lista de numeros de entrada

    Returns:
        list: lista de numeros al cuadrado
    '''
    square_list = [x**2 for x in num_list]
    return square_list
  

if __name__ == '__main__':
    lista_al_cuadrado = calculate_square([2, 3, 5, 7, 11])
    print(lista_al_cuadrado)