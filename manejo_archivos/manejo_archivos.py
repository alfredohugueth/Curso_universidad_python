# Abrir un archivo ya existente, o crear un archivo, w significa escribir
try:
    archivo = open('prueba.txt', 'w', encoding='utf8')
    archivo.write('Agregamos información al archivo\n')
    archivo.write('Adios')
except Exception as e:
    print(e)
finally:
    archivo.close() # Se cierra el archivo, ya no se puede trabajar con este archivo
    print('Fin del archivo')