'''
Reto 97: Crea una funcion que use argumentos arbitrarios de tipo
Keyword para recibir los 3 lados de un triangulo y calcule su perimetro
Imprime el resultado en un numero de punto flotante  
'''
def perimeter_triangle(**args):
    arg_list = [k for (j, k) in args.items()]
    return float(sum(arg_list))
    
if __name__ == '__main__':
    perimeter1 = perimeter_triangle(side1=5.2, side2=6, side3=4)
    print(perimeter1)