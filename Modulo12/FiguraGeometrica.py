class FiguraGeometrica:
    def __init__(self, ancho, alto) -> None:
        if self._validar_valor(ancho):
            self._ancho = ancho
        else:
            self._ancho = 0
        if self._validar_valor(alto):
            self._alto = alto
        else:
            self._alto = 0
                
    
    @property
    def ancho(self) -> float:
        return self._ancho
    
    @property
    def alto(self) -> float:
        return self._alto
    
    @ancho.setter
    def ancho(self, ancho):
        if self._validar_valor(ancho):
            self._ancho = ancho
        else:
            print(f'Valor invalido para el ancho: {ancho}')
    
    @alto.setter
    def alto(self, alto):
        if self._validar_valor(alto):
            self._alto = alto
        else:
            print(f'Valor invalido para el alto: {alto}')
            
    
    def __str__(self) -> str:
        return f'Figura Geometrica [ Ancho: {self._ancho}, Alto: {self._alto}]'
    
    def _validar_valor(self, valor) -> bool:
        return 0 < valor < 10 

    