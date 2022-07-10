def run():
    '''
    Utiliza una funcion lambda para capitalizar las
    palabras de una lista. Imprime el resultado en
    un nueva lista
    '''
    mensaje = ['llevo', 'sesenta', 'dias', 'programando', 'wiii']
    
    cap_mensaje = list(map(lambda x: x.capitalize(), mensaje))
    print(cap_mensaje)

if __name__ == '__main__':
    run()