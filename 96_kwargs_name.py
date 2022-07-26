'''
Reto 96: Crea una funcion que use argumentos arbitrarios de tipo
Keyword para recibir nombre, apellido y edad y devuelva estos
argumentos en un diccionario en el siguiente formato
{"nombre": "Pepito", "apellido": "Perez", "edad": 25} Imprime el
resultado 
'''
def name_age(**args):
    arg_dict = {j: k for (j, k) in args.items()}
    return arg_dict
    
if __name__ == '__main__':
    greet_list = name_age(nombre="Pepito", apellido="Perez", edad=25)
    print(greet_list)