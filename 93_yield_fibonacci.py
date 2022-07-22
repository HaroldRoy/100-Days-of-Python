'''
Reto 93: Crea una función que use yield y genere
los primeros 10 números de la serie de Fibonacci
[1, 1, 2, 3, 5, 8, 13, 21, 34, 55] Imprime el
resultado en una lista 
'''
def gen_fibo(n):
    n1, n2, count = 1, 1, 1
    while True:
        if count <= n:
            count += 1
            yield n1
            n1, n2 = n2, n1 + n2
        else:
            return
    

if __name__ == '__main__':
    lista = list(gen_fibo(10))
    print(lista)