x = 10
y = 2
z = x + y

print(x)
print(y)
print(z)

# Cada variable se almacena en la memoria RAM en una posicion de memoria
# La variable X apunta a una direccion de memoria donde esta el valor de 10 y asi respectivamente.

# Cada variable es una literal.

# Podemos obtener esa direccion de memoria con la funcion id ..
print(id(x))
print(id(y))
print(id(z))

# Estas direcciones de memoria son variables, por lo que cada vez que se ejecute el codigo, tendran un valor diferente