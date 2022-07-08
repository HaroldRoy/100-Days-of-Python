def run():
    '''
    Reto 20: La siguiente cadena: 'PpYyTtHhOoNnIiSsTtAa' Separa las
    mayúsculas y minúsculas sin usar ciclos en nuevas cadenas e imprime
    el resultado en una sola linea
    '''
    txt = 'PpYyTtHhOoNnIiSsTtAa'
    mayus = txt[::2]
    minus = txt[1::2]

    print(mayus, minus) 

if __name__ == '__main__':
    run()