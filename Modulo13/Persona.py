class Persona:
    contador_personas = 0


    @classmethod
    def generar_siguiente_valor(cls):

        cls.contador_personas += 1
        return cls.contador_personas

    def __init__(self, nombre, edad) -> None:
        
        self.id_persona = Persona.generar_siguiente_valor()
        self.nombre = nombre
        self.edad = edad

    def __str__(self) -> str:
        
        return f'Persona: [{self.id_persona} {self.nombre} {self.edad}]'
    

persona_1 = Persona('Alfredo', 22)
persona_2 = Persona('Carlos', 23)

print( persona_1 )
print( persona_2 )