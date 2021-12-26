# Tarea 11

def multiplicar(*args):
    resultado = 1
    for numero in args:
        resultado *= numero
    return resultado

respuesta = multiplicar(1,2,3,4,5)
print(f'La respuesta de multiplicar todos los valores de entrada es: {respuesta}')