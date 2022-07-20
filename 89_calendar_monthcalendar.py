import calendar

def run():
    '''
    Reto 89: Utiliza calendar para obtener los días
    lunes del mes Julio del año 2022
    '''
    num_weeks = [x[0] for x in calendar.monthcalendar(2022, 7) if x[0] != 0]
    print(num_weeks)


if __name__ == '__main__':
    run()