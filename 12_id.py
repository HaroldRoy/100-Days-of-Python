def run():
    '''
    Reto 12: Intercambia los valores de dos variables e imprime su ubicación
    en memoria utilizando la funcion id()
    '''
    var1 = 1
    var2 = 2
    var1, var2 = var2, var1
    
    print(id(var1), id(var2))
    
if __name__ == '__main__':
    run()