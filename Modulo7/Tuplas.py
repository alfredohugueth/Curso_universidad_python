# Una lista es modificable
# Una tupla no es modificable, es decir inmutable, No podemos agregar, eliminar o modificar elementos a la tupla

frutas = ('Naranja', 'Platano', 'Guayaba')

# Saber el largo
print(len(frutas))

# Respeta el orden en el que son agregados a la tupla
print(frutas)

# Acceder a un elemento
print(frutas[0])

# Navegacion inversa
print(frutas[-1])

# Acceder a un rango
print(frutas[0:1]) # Cuando una tupla solo tiene un valor, debe de tener la siguiente estructura ( elemento, )

# Recorrer elemento de una tupla
for fruta in frutas:
    print(fruta, end=' ')

# Cambiar valor de una tupla
# frutas[0] = 'Pera'

# Podemos convertir nuestra tupla a una lista
frutaLista = list(frutas)
frutaLista[0] = 'Pera'
frutas = tuple(frutaLista)

print('\n' ,frutas)

# Eliminar la tupla por completo
del frutas