import random

def run():
    '''
    Reto 50: Genera 5 numeros enteros de forma aleatoria.
    Almacenalos en una lista Sumalos e imprime el resultado
    '''
    num_list = []
    
    for n in range(0, 5):
        n = random.randint(1, 100)
        num_list.append(n)

    print(sum(num_list))

    # lista_random = [random.randint(0, 100) for i in range(5)]

if __name__ == '__main__':
    run()