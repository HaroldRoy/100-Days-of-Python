import calendar

def run():
    '''
    Reto 88: Utiliza calendar para imprimir la cantidad
    de semanas en cada mes del año 2022
    '''
    num_weeks = [len(calendar.monthcalendar(2022, x)) for x in range(1, 13)]
    print(num_weeks)

if __name__ == '__main__':
    run()