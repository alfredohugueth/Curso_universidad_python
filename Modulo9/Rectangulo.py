class Rectangulo:
    """
    Crea un objeto Rectangular con Base b y altura a
    y calcula su area
    """
    def __init__(self, base, altura) -> None:
        self.base = base
        self.altura = altura

    def calcular_area(self) -> int:
        return self.base * self.altura

rectangulo_1 = Rectangulo(3,2)
print(f'El area del rectangulo es: {rectangulo_1.calcular_area()}')