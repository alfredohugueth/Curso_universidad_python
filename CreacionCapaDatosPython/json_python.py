# Leer archivo JSON
# JSON = JavaScript Object Notation
import json
import urllib.request

respuesta = urllib.request.urlopen('https://jsonplaceholder.typicode.com/todos')
print(respuesta)
cuerpo_respuesta = respuesta.read()
print(cuerpo_respuesta)

# Procesamos la respuesta

json_respuesta = json.loads(cuerpo_respuesta.decode('utf-8'))
print(json_respuesta)

# Imprimir solo los nombres de las personas
# JSON se convierte a listas y diccionarios en python
for objeto in json_respuesta:
    print(f'Data: [UserID:{objeto["userId"]}]')