from datetime import datetime

def run():
    '''
    Reto 84: Utiliza datetime para convertir la cadena
    '12-07-2022' a timestamp. Imprime el resultado
    '''
    my_date = '12-07-2022'
    
    format_date = datetime.strptime(my_date, '%d-%m-%Y')
    timestamp_date = datetime.timestamp(format_date) 
    print(timestamp_date)


if __name__ == '__main__':
    run()