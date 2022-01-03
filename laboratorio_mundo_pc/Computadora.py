from Teclado import Teclado
from Raton import Raton
from Monitor import Monitor

class Computadora:
    contador_computadoras = 0

    def __init__(self, nombre, monitor, teclado, raton) -> None:
        self._id = Computadora.obtener_id()
        self._nombre = nombre
        self._monitor = monitor
        self._teclado = teclado
        self._raton = raton
        
    
    @classmethod
    def obtener_id(cls):
        cls.contador_computadoras += 1
        return cls.contador_computadoras
    
    def __str__(self) -> str:
        return f'''
        {self._nombre}: {self._id}
        {self._monitor}
        {self._teclado}
        {self._raton}
        '''

if __name__ == '__main__':

    teclado_1 = Teclado('USB', 'HP')
    raton_1 = Raton('USB', 'HP')
    monitor_1 = Monitor('HP', 12)
    computadora = Computadora('Prueba', monitor_1, teclado_1, raton_1)

    print(computadora)
