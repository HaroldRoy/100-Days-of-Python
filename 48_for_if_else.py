import random

def run():
    '''
    Reto 48: Con un rango de 5 numeros crea una lista
    que refleje con valores booleanos cuales son pares
    e imprime el resultado 
    '''
    num_list = list(range(1, 6))
    bool_list = []

    for num in num_list:
        if num % 2 == 0:
            bool_list.append(True)
        else:
            bool_list.append(False)

    print(bool_list)

if __name__ == '__main__':
    run()