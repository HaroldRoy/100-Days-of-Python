import datetime

def run():
    '''
    Reto 81: Utiliza datetime para agregarle a la
    fecha actual 7 días más. Imprime el resultado 
    '''
    today_date = datetime.date.today()
    print(today_date + datetime.timedelta(days=7))
    

if __name__ == '__main__':
    run()