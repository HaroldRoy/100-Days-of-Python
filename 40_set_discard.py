def run():
    '''
    Reto 40: Utiliza el conjunto del reto anterior y elimina
    al gato del conjunto, si es que existiera, sin usar
    sentencias condicionales e imprime el resultado. 
    '''
    anm_set = {'leon', 'elefante', 'condor', 'jaguar', 'mono'}
    
    anm_set.discard('gato')
    print(anm_set)

if __name__ == '__main__':
    run()