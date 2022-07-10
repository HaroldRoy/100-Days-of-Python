def run():
    '''
    Reto 57: Utiliza una funcion lambda para encontrar los
    multiplos de 3 en la lista de numero. Imprime el resultado
    en un nueva lista
    '''

    list_num = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    mult_three = list(filter(lambda x: (x % 3 == 0), list_num))
    print(mult_three)

if __name__ == '__main__':
    run()