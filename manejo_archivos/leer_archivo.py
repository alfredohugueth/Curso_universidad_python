# r -> Read. Opens a file for reading, Error if the file does not exist
# a -> Append. Opens a file for appending, creates the file if it does not exist
# w -> Write. Opens a file for writing, creates the file if it does not exist
# x -> Create. Creates the specified file, returns an error if the file exist
# t -> Text. Text mode file
# b -> Binary. Binary mode ex: Images
from os import O_EXCL


archivo = open('prueba.txt', 'r', encoding='utf8')
# print(archivo.read()) 

# Leer algunos caracteres
# print(archivo.read(5))
# print(archivo.read(5))

# Leer lineas completas
# print(archivo.readline())
# print(archivo.readline())

# Leer por linea
# for linea in archivo:
#     print(linea)

# leer lineas, regresa una lista
# print(archivo.readlines())

# Acceder a una linea de la lista
# print(archivo.readlines()[1])

# Abrimos un nuevo archivo
# a - anexar informacion
archivo2 = open('copia.txt', 'a', encoding='utf8')
archivo2.write( archivo.read() )

archivo.close()
archivo2.close()

