from FiguraGeometrica import FiguraGeometrica
from Color import Color
class Cuadrado(FiguraGeometrica, Color): # El orden importa
    
    def __init__(self,color, lado) -> None:
        FiguraGeometrica.__init__(self, lado, lado) # Se inicializan cada clase padre de esta parte
        Color.__init__(self, color)
    
    def calcular_area(self) -> float:
        return self.alto * self.ancho
    
    def __str__(self) -> str:
        return f'{FiguraGeometrica.__str__(self)} {Color.__str__(self)} '