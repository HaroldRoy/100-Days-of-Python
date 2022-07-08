def run():
    '''
    Reto 42: Utiliza el conjunto del reto anterior, para
    encontrar la union de ambos conjuntos sin usar ciclos
    e imprime el resultado.
    '''
    anm_set = {'leon', 'elefante', 'condor', 'jaguar', 'mono'}
    pets_set = {'gato', 'perro', 'perico', 'pez', 'hamster'}

    set_uni = anm_set.union(pets_set)
    print(set_uni)

if __name__ == '__main__':
    run()