# Una funcion recursiva es una funcion que se llama a si misma para completar una tarea
# Es necesario un punto de ruptura en este tipo de funciones
def factorial(numero):
    if numero == 1:
        return 1
    else:
        return numero * factorial(numero-1)

numero1 = 3
resultado = factorial(numero1)
print(f'El factorial de {numero1} es: {resultado}')