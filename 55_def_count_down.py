def count_down(start_num: int):
    '''
    Funcion que hace cuenta regresiva a 0.
    Args:
        start_num (int): numero que inicia la cuenta

    Returns:
        print de el valor de la cuenta en cada iteracion
    '''
    if start_num == 0:
        print(0)
    else:
        print(start_num)
        count_down(start_num - 1)


if __name__ == '__main__':
    count_down(5)
