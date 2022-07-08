def run():
    '''
    Reto 26: Utiliza la función copy() para crear una copia de la lista de
    compras utilizada en el reto anterior, compara sus ids en memoria e
    imprime el resultado
    '''
    shop_list = ['noodles', 'garlic', 'chili', 'tomatoes', 'butter', 'ginger', 'flour']
    list_copy = shop_list.copy()
    
    print(id(shop_list) == id(list_copy)) 
    
if __name__ == '__main__':
    run()