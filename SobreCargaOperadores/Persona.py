class Persona:
    def __init__(self, nombre, edad) -> None:
        self.nombre = nombre
        self.edad = edad
    
    def __add__(self, other): # other es el elemento al lado derecho del operando
        return f'{self.nombre} {other.nombre}'
    
    def __sub__(self, other):
        return self.edad - other.edad

persona_1 = Persona('Juan', 22)
persona_2 = Persona('Carlos', 34)

print( persona_1 + persona_2 ) 

print( persona_1 - persona_2 )