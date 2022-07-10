import re

def run():
    '''
    Reto 63: Utiliza Regex para validar que las cadenas solo contengan
    caracteres alfanumericos. Imprime una lista con las cadenas validas
    '''
    my_list = [
        'Python3.10',
        'Python3',
        'ProgramandoAndo',
        'jun2022',
        '#100diasdecodigo',
        'Felicidades!']

    filter = '^[a-zA-Z0-9]*$'
    valid_mail = [e for e in my_list if re.search(filter, e)]
    print(valid_mail)


if __name__ == '__main__':
    run()
