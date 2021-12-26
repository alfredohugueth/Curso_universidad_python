# Cuando no se sabe el numero de parametros que debemos enviar
# Para argumentos variables
# Normalmente encontraremos *args como parametro de entrada para estos casos
def listar_nombres(*nombres):
    for nombre in nombres:
        print(nombre)

listar_nombres('Juan', 'Carla', 'Maria', 'Ernesto')
listar_nombres('Laura', 'Carlos')