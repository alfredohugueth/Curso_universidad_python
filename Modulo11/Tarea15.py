class Vehiculo:
    def __init__(self, color, ruedas) -> None:
        self._color = color
        self._ruedas = ruedas
    
    @property
    def color(self) -> str:
        return self._color
    
    @property
    def ruedas(self) -> int:
        return self._ruedas
    
    def __str__(self) -> str:
        return f'Vehiculo [ Color: {self._color}, Ruedas: {self._ruedas}]'
    

class Coche(Vehiculo):
    def __init__(self, color, ruedas, velocidad) -> None:
        super().__init__(color, ruedas)
        self._velocidad = velocidad
    
    @property
    def velocidad(self) -> float:
        return self._velocidad
    
    def __str__(self) -> str:
        return f'{super().__str__()}, Coche [ Velocidad: {self._velocidad}]'
    
class Bicicleta(Vehiculo):
    def __init__(self, color, ruedas, tipo) -> None:
        super().__init__(color, ruedas)
        self._tipo = tipo
    
    @property
    def tipo(self) -> str:
        return self._tipo
    
    def __str__(self) -> str:
        return f'{super().__str__()}, Bicicleta [ Tipo: {self._tipo}]'
