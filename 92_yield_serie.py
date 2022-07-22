'''
Reto 92: Crea una función que use yield y genere
la siguiente serie [1, 2, 3, 2, 1, 2, 3, 2, 1]
Imprime el resultado en una lista
'''

def num_serie(limite):
    i = 0
    
    count = 0
    direction = 1

    while i < limite:
        count += direction
        yield count
        if count == 3:
            direction = -1
        elif count == 1:
            direction = +1
        i += 1

if __name__ == '__main__':
    lista = list(num_serie(9))
    print(lista)