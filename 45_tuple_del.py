def run():
    '''
    Usa la tupla del ejemplo anterior, elimina los
    primeros 2 elementos e imprime el resultado
    PD. Las tuplas son inmutables.
    '''
    my_tuple = ('μ', 'E', 'S', 'Cp', 'λ')
    
    my_tuple = my_tuple[2:]
    print(my_tuple)


if __name__ == '__main__':
    run()