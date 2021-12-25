# Listas en python
nombres = ['Juan', 'Karla', 'Ricardo', 'Maria']
# Imprimimos la lista de nombres
print(nombres)

# Acceder de manera individual
print(nombres[1])

# Acceder a los elementos de manera inversa.
print(nombres[-1])

# Acceder a un rango de nuestros valores
print(nombres[0:2]) # Recuperara los elementos 0 y 1

print(nombres[:3]) # Recorre la lista desde el inicio hasta el indice 3 pero sin incluirlo

print(nombres[1:]) # Desde el indice indicado hasta el final

# Cambiar un valor de nuestra lista

nombres[3] = 'Ivone'
print(nombres)

# Iterar una lista
for nombre in nombres:
    print(nombre)
else:
    print('No existen mas nombres en la lista')

# Preguntar el largo de una lista
print(len(nombres))

# Agregar elemento a una lista
nombres.append('Lorenzo')
print(nombres)

# Insertar un elemento en un indice en especifico
nombres.insert(1, 'Octavio')
print(nombres)

# Remover un elemento
nombres.remove('Octavio')
print(nombres)

# Remover el ultimo elemento agregado a la lista
nombres.pop()
print(nombres)

# Eliminar un elemento en un indice indicado
del nombres[0]
print(nombres)

# Limpiar los elementos de la lista
nombres.clear()
print(nombres)

# Borrar lista por completo
del nombres
print(nombres)