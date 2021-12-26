# Para recibir un diccionario
# Un diccionario es indicado con **
def listar_terminos(**args):
    for key, value in args.items():
        print(f'{key}: {value}')

listar_terminos(IDE='Integrated Development Enviroment', PK='Primary Key')

