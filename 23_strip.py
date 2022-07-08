def run():
    '''
    Reto 23: Utiliza funciones de cadenas para quitar los
    espacios inecesarios de la siguiente cadena:
    "       Python es divertido       "
    '''
    TXT = "       Python es divertido       "
    word = TXT.strip()

    print(word)

if __name__ == '__main__':
    run()