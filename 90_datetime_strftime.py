from datetime import datetime

def run():
    '''
    Reto 90: Utiliza datetime para imprimir la fecha y hora
    en formato de 12 horas ejemplo "2022/07/18 11:30 PM"
    Imprime el resultado en una cadena 
    '''
    today_date = datetime.now()
    format_date = today_date.strftime("%Y/%m/%d %I:%M %p")
    print(format_date) 

if __name__ == '__main__':
    run()