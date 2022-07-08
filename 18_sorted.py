from tkinter.tix import TEXT


def run():
    '''
    Reto 18: Declara una variable de tipo cadena, encuentra el primer y último
    carácter en orden lexicográfico sin usar ciclos e imprimelos. 
    '''
    txt = 'murcielago'
    txt_lex = sorted(txt)

    print(txt_lex[0], txt_lex[-1])
    print(min(txt), max(txt))
if __name__ == '__main__':
    run()