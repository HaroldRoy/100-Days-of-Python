def transform_to_binary(num: int):
    '''
    Funcion que transforma numeros enteros a binario.
    Args:
        num (integer): numero de entrada entero

    Returns:
        string: cadena del valor del numero en binario
    '''
    list_modulos = []

    while num != 0:
        modulo = num % 2
        cociente = num // 2
        list_modulos.insert(0, modulo)
        num = cociente

    return "".join(map(str, list_modulos))


if __name__ == '__main__':
    num_bin = transform_to_binary(52)
    print(num_bin)