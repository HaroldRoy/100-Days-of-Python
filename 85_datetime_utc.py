from datetime import datetime

def run():
    '''
    Reto 85: Utiliza datetime para imprimir la fecha
    y hora actual en UTC
    '''
    today_date = datetime.utcnow()
    print(today_date)


if __name__ == '__main__':
    run()