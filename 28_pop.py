def run():
    '''
    Utiliza la lista de compras del reto anterior para
    remover el primer elemento de la lista sin usar
    ciclos e imprime la lista
    '''
    shop_list = ['noodles', 'garlic', 'chili', 'tomatoes', 'butter', 'ginger', 'flour']
    
    shop_list.pop(0)
    print(shop_list)

if __name__ == '__main__':
    run()