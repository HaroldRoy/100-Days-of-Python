def run():
    '''
    Reto 33: Declara una cadena que sea un palindromo y verifica
    que lo sea sin usar funciones adicionales. Imprime el resultado
    en una sola linea 
    '''
    txt = 'Anita laba la tina'

    txt_pal = txt.replace(' ', '').lower()
    print(txt_pal[::] == txt_pal[::-1])


if __name__ == '__main__':
    run()