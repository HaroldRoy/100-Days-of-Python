def vowels_in_dict(string_list: list):
    '''
    Funcion que cuenta la cantidad de vocales de cada cadena
    en un diccionario
    Args:
        string_list (list): lista de cadenas de entrada

    Returns:
        dict: diccionario de llave la cadena de la lista de entrada
        y de valor la cantidad de vocales
    '''
    dict_vowels = {}

    for palabra in string_list:
        contador = 0
        for letra in palabra:
            if letra.lower() in 'aeiou':
                contador += 1 
                dict_vowels[palabra] = contador  
    
    return dict_vowels


if __name__ == '__main__':
    print(vowels_in_dict(['Python', 'es', 'cool']))