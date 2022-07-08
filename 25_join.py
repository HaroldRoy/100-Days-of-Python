def run():
    '''
    Reto 25: Utiliza la lista de compras del reto anterior para
    construir una cadena con saltos de línea sin usar ciclos
    '''
    shop_list = ['noodles', 'garlic', 'chili', 'tomatoes', 'butter', 'ginger', 'flour']
    txt_sep = '\n'.join(shop_list)
    
    print(txt_sep) 
    
if __name__ == '__main__':
    run()