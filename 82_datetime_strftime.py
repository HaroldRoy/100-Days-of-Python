from datetime import datetime

def run():
    '''
    Reto 82: Utiliza datetime para imprimir la fecha y hora
    actual en el formato "10 July 2022, 12:12:12 AM". Imprime
    el resultado en una cadena
    '''
    today_date = datetime.now()
    format_date = today_date.strftime("%d %B %Y, %H:%M:%S %p")
    print(format_date)


if __name__ == '__main__':
    run()