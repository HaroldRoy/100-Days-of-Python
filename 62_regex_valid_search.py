import re

def run():
    '''
    Reto 62: Utiliza Regex para validar la lista de emails. Imprime
    una lista con los emails validos.
    '''
    mail_list = ['pythonlapaz@gmail.com', 'dias.com', 'comidita@.com', 'programando@outlook.com']

    filter = '^[a-z0-9]+[\._]?[a-z0-9]+[@]\w+[.]\w{2,3}$'
    valid_mail = [m for m in mail_list if re.search(filter, m)]
    print(valid_mail)


if __name__ == '__main__':
    run()