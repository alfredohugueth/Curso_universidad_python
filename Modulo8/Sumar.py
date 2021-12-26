# Funcion para sumar dos parametros a y b

def sumar(a : int = 0, b: int = 0) -> int:
    return a + b


resultado = sumar(1, 2)

print(f'Resultado de la suma: {resultado}')

resultado2 = sumar()

print(f'Resultado de la suma: {resultado2}')
