'''
Reto 98: Utiliza timeit para obtener el tiempo de
ejecucion de la siguiente funcion. Imprime el
resultado en una sola linea
'''
import timeit

my_code = '''
def lazy():
    suma = 0
    for i in range(0, 50000000):
        suma += i
'''


if __name__ == '__main__':
    print(timeit.timeit(stmt = my_code))





# Other solution

# import timeit

# def lazy():
#     suma = 0
#     for i in range(0, 50000000):
#         suma += i

# start = timeit.default_timer()
# lazy()
# end = timeit.default_timer()
# print(end - start)