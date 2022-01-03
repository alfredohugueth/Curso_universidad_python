
class DispositivoEntrada:
    def __init__(self, tipoEntrada, marca) -> None:
        self._tipoEntrada = tipoEntrada
        self._marca = marca
    
    @property
    def tipoEntrada(self):
        return self._tipoEntrada
    
    @property
    def marca(self):
        return self._marca
    
    @tipoEntrada.setter
    def tipoEntrada(self, tipoEntrada):
        self._tipoEntrada = tipoEntrada
    
    @marca.setter
    def marca(self, marca):
        self._marca = marca
    
    def __str__(self) -> str:
        return f'marca: {self._marca}, tipo_entrada: {self._tipoEntrada}'


if __name__ == '__main__':
    entrada_1 = DispositivoEntrada('USB', 'HP')
    print(entrada_1)
    
