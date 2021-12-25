# No mantiene un orden, No permite almacenar elementos duplicados, 
# No es posible modificar los elementos almacenados, pero si es posible agregar elementos o eliminarlos

# Set
planetas = {'Marte', 'Jupiter', 'Venus'}
print(planetas)

# Conocer el largo
print(len(planetas))

# Revisar si un elemento esta precente
print('Marte' in planetas)

# Agregar elementos a un Set
planetas.add('Tierra')
print(planetas)

# No soporta elementos duplicados
planetas.add('Tierra')
print(planetas)

# Eliminar elemento posiblemente arrojando un error
planetas.remove('Tierra') # Debe estar presente en el Set
print(planetas)

# Eliminar elemento solo si esta presente (No arroja error)
planetas.discard('Tierras')
print(planetas)

# Limpiar Set
planetas.clear()
print(planetas)

# Eliminar el Set de memoria
del planetas
print(planetas)
