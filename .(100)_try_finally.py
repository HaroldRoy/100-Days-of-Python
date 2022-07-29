'''
Reto 100: Utiliza try para capturar e imprimir la excepcion
dentro de la siguiente funcion y agrega un mensaje
final utilizando finally. En este reto si se aceptan
multiples print
'''

def dia100():
    mensaje = "LLegaste al último día"

    try:
        print(mensaje[len(mensaje)])
    except Exception as e:
        print("Error: {}".format(e))
    finally:
        print('¡Muchas gracias por todo su trabajo Python La Paz!')

if __name__ == '__main__':
    dia100()
