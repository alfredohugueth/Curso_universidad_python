from NumerosIdenticosException import NumerosIdenticosException
# Tenemos una clase padre BaseException

# Pero trabajaremos con su clase Hija Exception regularmente

# Los errores que podremos trabajar con estas clase son:
# AritmeticError, OSError, RuntimeError, LookupError, SyntaxError
resultado = None
try:
    a = int(input('Primer numero: '))
    b = int(input('Segundo numero: '))
    if a == b:
        raise NumerosIdenticosException('Numeros Identicos') # Para ejecutar una excepcion
    resultado = a/b # AritmeticError
    # Si ocurre un error, no se asigna la variable
except ZeroDivisionError as zde: 
    print(f'ZeroDivisionError - Ocurrio un error: {zde}')
except TypeError as tpe:
    print(f'TypeError - Ocurrio un error: {tpe}')
except Exception as e:
    print(f'Exception - Ocurrio un error: {e}') 
    # Es recomendable capturar con clases genericas, si es en el caso
    # La mas general debe de ir de ultima

# En caso de que no se haya lanzado ninguna excepcion, Es opcional
else:
    print('No se arrojó ninguna excepcion')

# Siempre se va a ejecutar ocurra o no una excepcion
finally:
    print('Ejecucion del bloque finally')



print(f'Resultado: {resultado}')
print('Continuamos...')