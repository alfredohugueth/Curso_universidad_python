from DispositivoEntrada import DispositivoEntrada
class Raton(DispositivoEntrada):
    contador_ratones = 0
    def __init__(self, tipoEntrada, marca) -> None:
        super().__init__(tipoEntrada, marca)
        self.__id_raton = Raton.obtener_id()
    
    @classmethod
    def obtener_id(cls):
        cls.contador_ratones += 1
        return cls.contador_ratones
    
    @property
    def id_raton(self) -> int:
        return self.__id_raton
    
    def __str__(self) -> str:
        return f'Id: {self.__id_raton}, {super().__str__()}'
    
if __name__ == '__main__':
    raton_1 = Raton('USB', 'Apple')
    print(raton_1)
    
