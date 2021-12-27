class Persona:
    # Self es una variable que se guarda en memoria que para almacenar la informacion de la clase
    # Puede tener otro nombre, como this
    # Los atributos con _ no deberian ser accesibles fuera de la clase.
    # Sin embargo es posible
    # Sirven como sugerencias
    # Si usamos __ estos atributos no son modificables

    # Las variables de solo lectura, solo tienen metodo get asociado @property
    def __init__(self, nombre, apellido, edad, *args, **kwargs) -> None: # Nos permite inicializar las clases
        self._nombre = nombre
        self._apellido = apellido
        self._edad = edad
        self._args = args
        self._kwargs = kwargs
    
    @property # Nos permite acceder acceder al metodo como si fuera un atributo, DECORADOR 
    def nombre(self) -> str:
        return self._nombre
    
    @nombre.setter # Decorador para modificar atributo de clase
    def nombre(self, nombre) -> None:
        self._nombre = nombre
    
    @property
    def apellido(self) -> str:
        return self._apellido
    
    @apellido.setter
    def apellido(self, apellido) -> None:
        self._apellido = apellido
    
    @property
    def edad(self) -> int:
        return self._edad
    
    @edad.setter
    def edad(self, edad) -> None:
        self._edad = edad

    
    
    def mostrar_detalle(self)-> None:
        print(f'Persona: {self._nombre} {self._apellido} {self._edad}')
    
    def __del__(self): # Metodo para ejecutar al eliminar el objeto de la clase
        print(f'Persona: {self._nombre} {self._apellido}')

    

# Esto evita que se ejecute el codigo inferior si no se esta realizando la prueba de este archivo especifico
if __name__ == "__main__": 
    persona_1 = Persona('Alfredo', 'Hugueth', 22) # Al crear el objeto, se llama indirectamente el metodo __init__
    persona_1.mostrar_detalle()

    # Se puede usar los metodos de clase, usando la clase pasando la referencia
    # Persona.mostrar_detalle(persona_1)

    # Podemos agregar atributos a la clase de manera dinamica
    # persona_1.telefono = '12345678'
    # print(persona_1.telefono)


    persona_2 = Persona('Karla', 'Gomez', 30)
    persona_2.mostrar_detalle()
