def run():
    '''
    Reto 49: Declara una variable numerica con valor 100
    Decramenta su valor de 10 en 10 mientras no sea 0 Imprime
    el valor de la variable cada iteracion 
    '''
    num = 100

    while num != 0:
        print(num)
        num -= 10
        
if __name__ == '__main__':
    run()