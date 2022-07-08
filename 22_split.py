def run():
    '''
    Reto 22: Utiliza funciones de cadenas para crear una lista
    de palabras con las siguiente cadena:
    'Los pequeños pasos te llevan a algo más grande'
    '''
    TXT = 'Los pequeños pasos te llevan a algo más grande'
    word_list = TXT.split(' ')

    print(word_list)

if __name__ == '__main__':
    run()