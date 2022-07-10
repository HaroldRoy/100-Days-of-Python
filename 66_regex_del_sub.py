import re

def run():
    '''
    Reto 66: Utiliza Regex para eliminar los caracteres que
    no sean alfanumericos en las cadenas de la lista. Imprime
    una lista con las cadenas limpias
    '''
    my_list = [
        'Python3.10',
        'Python3',
        'ProgramandoAndo',
        'jun2022',
        '#100diasdecodigo',
        'Felicidades!'
        ]

    alphanum_list = [re.sub('[^A-Za-z0-9]+', '', w) for w in my_list]
    print(alphanum_list)


if __name__ == '__main__':
    run()