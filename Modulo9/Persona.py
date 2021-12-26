class Persona:
    # Self es una variable que se guarda en memoria que para almacenar la informacion de la clase
    # Puede tener otro nombre, como this
    def __init__(self, nombre, apellido, edad, *args, **kwargs) -> None: # Nos permite inicializar las clases
        self.nombre = nombre
        self.apellido = apellido
        self.edad = edad
        self.args = args
        self.kwargs = kwargs
    
    def mostrar_detalle(self)-> None:
        print(f'Persona: {self.nombre} {self.apellido} {self.edad}')

    



persona_1 = Persona('Alfredo', 'Hugueth', 22) # Al crear el objeto, se llama indirectamente el metodo __init__
persona_1.mostrar_detalle()

# Se puede usar los metodos de clase, usando la clase pasando la referencia
# Persona.mostrar_detalle(persona_1)

# Podemos agregar atributos a la clase de manera dinamica
persona_1.telefono = '12345678'
print(persona_1.telefono)


persona_2 = Persona('Karla', 'Gomez', 30)
persona_2.mostrar_detalle()
