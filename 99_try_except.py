def run():
    '''
    Reto 99: Utiliza try para capturar e imprimir la excepcion
    de una division entre 0 del siguiente fragmento de codigo
    '''
    a = 7
    try:
        b = a / 0
    except Exception as e:
        print("Error: {}".format(e))

if __name__ == '__main__':
    run()