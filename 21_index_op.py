def run():
    '''
    Reto21: Utiliza lo aprendido en el reto anterior para
    encontrar el mensaje escondido en:
    hjfacetiluzislcafiesdolavedfiedesno
    '''
    TXT = 'hjfacetiluzislcafiesdolavedfiedesno'
    txt_unlk = TXT[2::3]

    print(txt_unlk)

if __name__ == '__main__':
    run()