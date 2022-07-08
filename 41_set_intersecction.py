def run():
    '''
    Reto 41: Utiliza el conjunto del reto anterior, define
    un nuevo conjunto de mascotas, encuentra su interseccion
    de ambos conjuntos sin usar ciclos e imprime el resultado
    '''
    anm_set = {'leon', 'elefante', 'condor', 'jaguar', 'mono'}
    pets_set = {'gato', 'perro', 'perico', 'pez', 'hamster'}

    print(anm_set & pets_set)

if __name__ == '__main__':
    run()