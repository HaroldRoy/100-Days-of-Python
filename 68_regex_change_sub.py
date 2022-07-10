import re

def run():
    '''
    Reto 68: Utiliza Regex para cambiar el formato de las fechas
    de YYYY-MM-DD a DDMMYYYY de las fechas de la lista. Imprime
    una lista con las fechas con el nuevo formato
    '''
    dates_list = [
        '2022-12-05',
        '1993-06-12',
        '2005-01-26',
        '2021-10-08'
        ]

    dates_correct = [re.sub('(\d{4})-(\d{1,2})-(\d{1,2})', '\\3\\2\\1', d) for d in dates_list]
    print(dates_correct)


if __name__ == '__main__':
    run()