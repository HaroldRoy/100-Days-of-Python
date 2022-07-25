'''
Reto 95: Crea una funcion que use argumentos arbitrarios para
recibir N-numeros y determine cual es el mayor y el menor y los
devuelva en un diccionario en el siguiente formato {"mayor": 5,
"menor": -10} Imprime el resultado   
'''
def max_min(*numbers):
    min = max = numbers[0]
    for num in numbers:
        if num < min:
            min = num
        elif num > max:
            max = num
    return {"mayor": max, "menor": min}

     
if __name__ == '__main__':
    num_list = max_min(5, 4, 2, -2, -10, -6)
    print(num_list)

# Easier solution

# def mayor_menor(*numeros):
#     mayor = max(numeros)
#     menor = min(numeros)
#     return {"mayor": mayor, "menor": menor}

# print(mayor_menor(5, 4, 2, -2, -10, -6))