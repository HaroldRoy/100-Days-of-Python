from datetime import datetime

def run():
    '''
    Reto 83: Utiliza datetime para convertir la fecha
    "Jul 11 2022 1:30AM" al formato "2022-07-11 01:30:00"
    Imprime el resultado 
    '''
    my_date = 'Jul 11 2022 1:30AM'
    
    format_date = datetime.strptime(my_date, '%b %d %Y %I:%M%p')
    new_date = format_date.strftime("%Y-%m-%d %H:%M:%S")
    print(new_date)


if __name__ == '__main__':
    run()