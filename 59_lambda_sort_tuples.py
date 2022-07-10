def run():
    '''
    Reto 59: Utiliza la funcion lambda para ordenar de forma
    ascendente la siguiente lista de tuplas tomando el valor
    numerico como referencia. Imprime el resultado
    '''
    tuple_notes = [('Química', 88), ('Física', 90), ('Lenguaje', 97)]
    tuple_notes.sort(key = lambda x: x[1])
    print(tuple_notes)    

if __name__ == '__main__':
    run()