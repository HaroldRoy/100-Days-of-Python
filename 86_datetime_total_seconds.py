from datetime import datetime

def run():
    '''
    Reto 86: Utiliza datetime para calcular la cantidad
    de segundos que han pasado desde el inicio del reto
    considerando solo la fecha. Considera que el reto
    inicio el "20/04/2022". Imprime el resultado 
    '''
    start_date = '2022/04/20'

    d1 = datetime.strptime(start_date, "%Y/%m/%d").date()
    d2 = datetime.now().date()
    delta = d2 - d1
    print(delta.total_seconds())
    

if __name__ == '__main__':
    run()