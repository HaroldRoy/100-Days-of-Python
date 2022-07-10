import re

def run():
    '''
    Reto 69: Utiliza Regex para extraer todas las 'a' seguidas de
    una o más 'b's de la siguiente cadena
    'abholaaaaabaaabbpythonistaaaaaabbbbb' Imprime una lista con
    las subcadenas extraidas
    '''
    txt = 'abholaaaaabaaabbpythonistaaaaaabbbbb'

    # matches = re.findall(r'(a+)(b)', txt)
    # matches_list = [x + y for x, y in matches]
    # print(matches_list)

    patron = 'a+b'
    subcadenas = re.findall(patron, txt)
    print(subcadenas)


if __name__ == '__main__':
    run()