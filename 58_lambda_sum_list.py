def run():
    '''
    Reto 58: Utiliza una funcion lambda para sumar las
    listas. Imprime el resultado 
    '''

    list_a = [2, 4, 5]
    list_b = [6, 7, 1]
    list_sum = list(map(lambda a, b: a + b, list_a, list_b))
    print(list_sum)

if __name__ == '__main__':
    run()