def num_square(lenght):
    '''
    Función generadora que retorna el cuadrado de
    el rango de numeros que se ingrese
    Args:
        lenght(int): rango de números

    Returns:
        generator object: objeto que produce
        los numeros al cuadrado 
    '''
    for num in range(1, lenght + 1):
        yield num**2

if __name__ == '__main__':
    square_list = [num for num in num_square(10)]
    print(square_list)


# Solución publicada
# def cuadrados(limite):
#     i = 1
#     while i <= limite:
#         yield i*i
#         i += 1

# lista = list(cuadrados(10))
# print(lista)