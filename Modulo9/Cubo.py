class Cubo:

    """
    Crea un objeto cubo con Base b, altura h y profundidad p
    permite calcular el volumen del mismo
    """

    def __init__(self, base, altura, profundidad) -> None:
        self.base = base
        self.altura = altura
        self.profundidad = profundidad
    
    def calcular_volumen(self) -> int:
        return self.base * self.altura * self.profundidad


cubo_1 = Cubo(2, 3, 4)
print(f'El volumen del cubo es: {cubo_1.calcular_volumen()}')