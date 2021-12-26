# Crear una función para calcular el total de un pago incluyendo un impuesto aplicado.
# La función se llama calcular_total()
# La función recibe dos parámetros:
# 1. pago_sin_impuesto
# 2. Impuesto (De mamera porcentual. 10 significa 10%)

def calcular_total( pago_sin_impuesto: int = 0, impuesto: int = 0):
    return pago_sin_impuesto + (pago_sin_impuesto*impuesto/100)

pago_sin_impuesto = 1000
impuesto = 20
resultado = calcular_total( pago_sin_impuesto, impuesto)
print(f'El resultado de aplicarle un impuesto del {impuesto}% a {pago_sin_impuesto} es: {resultado}')
