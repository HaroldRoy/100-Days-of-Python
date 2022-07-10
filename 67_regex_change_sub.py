import re

def run():
    '''
    Reto 67: Utiliza Regex para cambiar el formato de las fechas
    de YYYYMMDD a YYYY-MM-DD de las fechas de la lista. Imprime
    una lista con las fechas
    '''
    my_list = [
        '20221205',
        '19930612',
        '20050126',
        '20211008'
        ]

    alphanum_list = [re.sub('(\d{4})((\d{2}))', r'\1-\2-', w) for w in my_list]
    print(alphanum_list)


if __name__ == '__main__':
    run()