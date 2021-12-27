from Persona import Persona

print('Creacion objetos'.center(50, '-')) # Dar formato a los textos
persona_1 = Persona('Karla', 'Gomez', 30)
persona_1.mostrar_detalle()

print('Eliminacion de objetos'.center(30, '-'))
del persona_1