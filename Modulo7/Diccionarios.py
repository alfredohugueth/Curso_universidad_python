# Tendremos una llave y un valor asociado a dicha llave (key, value)

diccionario = {
    'IDE': 'Integrated Development Enviroment',
    'OOP': 'Object Oriented Programming',
    'DBMS': 'Database Management System'
}

print(diccionario)

# Conocer el largo del dict
print(len(diccionario))

# Acceder a un elemento (key)
print(diccionario['IDE'])

# Otra forma de recuperar un elemento
print(diccionario.get('OOP'))

# Modificar elementos en un diccionario
diccionario['IDE'] = 'integrated development enviroment'
print(diccionario)

# Recorrer elementos en un diccionario
for termino, valor in diccionario.items():
    print(termino, valor)


for termino in diccionario.keys():
    print(termino)

for valor in diccionario.values():
    print(valor)


# Comprobar existencia de un elemento
print('IDE' in diccionario)

# Agregar elemento al diccionario
diccionario['PK'] = 'Primary Key'
print(diccionario)

# Remover elemento de un diccionario
diccionario.pop('DBMS')
print(diccionario)

# Limpiar
diccionario.clear()

# Eliminar diccionario
del diccionario
