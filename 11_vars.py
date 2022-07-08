def run():
    '''
    Reto 11: Declara una variable númerica y una de tipo cadena, intercambia los
    valores de ambas e imprime el resultado en una sola linea 
    '''
    num = 12
    txt = 'doce'
    
    num, txt = txt, num
    print(num, txt)

if __name__ == '__main__':
    run()