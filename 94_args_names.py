'''
Reto 94: Crea una función que use argumentos arbitrarios
para recibir N-cadenas de nombres y devuelva una lista de
N-saludos ejemplo de salida ['Hola Katy', 'Hola Ariel']
Imprime el resultado en una lista 
'''
def greetings(*args):
    name_list = [f"Hola {name}" for name in args]
    return name_list
    
if __name__ == '__main__':
    greet_list = greetings('Katy', 'Ariel', 'Marco', 'Raysa')
    print(greet_list)