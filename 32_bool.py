def run():
    '''
    Reto 32: Declara dos listas, una vacia y otra con elementos
    convierte ambas listas en booleanos. Imprime el resultado
    en una sola linea 
    '''
    lst1 = []
    lst2 = ['cadena', 1, 4.24, 'otra cadena', 0]
    
    lst1_bl, lst2_bl = bool(lst1), bool(lst2) 

    print(lst1_bl, lst2_bl)

if __name__ == '__main__':
    run()