def run():
    '''
    Reto 31: Declara dos variables boleanos, convierte una
    en entero y la otra en cadena, imprime el resultado en
    una sola linea
    '''
    var1, var2 = True, False
    var1_int = int(var1)
    var2_str = str(var2)

    print(var1_int, var2_str)

if __name__ == '__main__':
    run()