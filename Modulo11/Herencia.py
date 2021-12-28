# La clase Hija hereda caracteristicas de la clase padre, ademas de tener sus propias caracteristicas
# Todas las clases heredan de la clase Object
# En python existe el concepto de herencia multiple
class Persona:
    def __init__(self, nombre, edad) -> None:
        self._nombre = nombre
        self._edad = edad
    
    @property
    def nombre(self) -> str:
        return self._nombre
    
    @property
    def edad(self) -> int:
        return self._edad
    
    def __str__(self) -> str: # Funcion que se ejecuta cuando se imprime el objeto, esta se puede sobreescribir
        return f'Persona: {self._nombre} {self._edad}'


class Empleado(Persona): # Esto indica que la clase empleado, hereda de la clase padre Persona

    def __init__(self, nombre, edad, sueldo) -> None:
        super().__init__(nombre, edad) # Metodo inicializador de la clase padre
        self._sueldo = sueldo
    
    @property
    def sueldo(self) -> int:
        return self.sueldo
    
    def __str__(self) -> str:
        return f'{super().__str__()} Sueldo: {self._sueldo}'




