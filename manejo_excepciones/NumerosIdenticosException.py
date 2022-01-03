# Podemos definir clases personalizadas para el manejo de excepciones:

class NumerosIdenticosException(Exception):
    
    def __init__(self, mensaje : str) -> None:
        self.message = mensaje
    