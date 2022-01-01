# Contexto dinamico, se asocia a los objetos creados a partir de la clase
# Contexto estatico, se asocia a los metodos de clase y metodos estaticos
# Desde el contexto dinamico se puede acceder a los metodos estaticos
# Sin embargo desde el contexto estatico no se puede acceder al contexto dinamico
class MiClase:

    variable_clase = 'Valor variable clase'

    def __init__(self, variable_instancia) -> None: 
        self.variable_instancia = variable_instancia
    
    # Metodos estaticos
    # No utilizan las variables de instancia, por lo que no utiliza la variable self
    @staticmethod
    def metodo_estatico():
        # Podemos acceder a nuestras variables de clase.
        print(MiClase.variable_clase)
    
    # Metodo de clase
    # No recibe la variable self, sino que recibe una variable cls, 
    # que indica que recibe la variable asociada a la clase
    @classmethod 
    def metodo_clase(cls):
        print(cls.variable_clase)
    
    

miClase = MiClase("Valor Instancia")

# Podemos definir variables de clase al vuelo = en cualquier momento
MiClase.variable_clase_2 = "Valor clase 2"


# Acceder a un metodo estatico
MiClase.metodo_estatico()

# Acceder a un metodo de clase
MiClase.metodo_clase()

# Tambien se pueden acceder a los metodos de clase desde un objeto
miClase.metodo_clase()