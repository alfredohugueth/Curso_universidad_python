# Esto facilita que no es necesario cerrar el archivo, ya que se hace automaticamente
# with open('prueba.txt', 'r', encoding='utf8') as archivo:
# from archivos_con_with.ManejoArchivos import ManejoArchivos
from ManejoArchivos import ManejoArchivos

with ManejoArchivos('prueba.txt') as archivo:
    print( archivo.read() ) 
    # El metodo __read__, se ejecuta cuando se llama la funcion read, 
    # El metodo __exit__, se ejecuta al final del with
    # Lo usaremos para el manejo de bases de datos

