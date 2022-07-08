def run():
    '''
    Reto 37: Utiliza el diccionario de palabras del reto
    anterior para eliminar todos los elementos del
    diccionario sin usar ciclos, imprime el resultado 
    '''
    dict_def = {
        'Algoritmo': 'Es un conjunto de instrucciones o reglas definidas y no-ambiguas, ordenadas y finitas que permite, típicamente, solucionar un problema, realizar un cómputo, procesar datos y llevar a cabo otras tareas o actividades.',
        'Librerias': 'Es un conjunto de subprogramas utilizados para desarrollar software.',
        'Operadores': 'Son símbolos que indica al compilador que realice operaciones lógicas o matemáticas específicas.',
        'Pseudocódigo': 'Es la representación narrativa de los pasos que debe seguir un algoritmo para dar solución a un problema determinado.',
        'Variable': 'Es una posición en memoria donde se puede almacenar un valor que se usará en el programa',
        'Python': 'Lenguaje de programación multiparafigma'
        }

    dict_def.clear()
    print(dict_def)

if __name__ == '__main__':
    run()