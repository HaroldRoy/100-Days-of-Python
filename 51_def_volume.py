import math

def volumen_cilindro(base, altura):
    '''
    Calcula el volumen de cilindro a partir de su base
    y su altura.
    '''
    volumen = math.pi*altura*(base/2)**2
    return volumen

if __name__ == '__main__':
    vol_cilindro_1 = volumen_cilindro(base = 5, altura = 7)
    print(vol_cilindro_1)

'''
Bienvenido al día 51....
'''

# from math import pi

# def volumen_cilindro(base: float, altura: float):
#     '''
#     Funcion que calcula el volumen de un cilindro
#     Args:
#         base (float): diametro del cilindro
#         altura (float): altura del cilindro
    
#     Returns:
#         float: volumen calculado del cilindro
#     '''
#     radio = base / 2
#     volumen = pi * (radio**2) * altura
#     return volumen

# volumen = volumen_cilindro(5, 7)
# print(volumen)