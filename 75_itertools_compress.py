import itertools

def run():
    '''
    Reto 75: Utiliza itertools para obtener el mensaje secreto
    en la siguiente cadena. Imprime el resultado en una cadena.
    '''
    chain = "P1y2t3h4o5n6!7"
    
    secret_list = list(itertools.islice(chain, 0, len(chain), 2))
    chain_secret = ''.join(secret_list)
    print(chain_secret)

    # cadena = 'P1y2t3h4o5n6!7'
    # selector = [1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1]
    # print(''.join(itertools.compress(cadena, selector)))

if __name__ == '__main__':
    run()