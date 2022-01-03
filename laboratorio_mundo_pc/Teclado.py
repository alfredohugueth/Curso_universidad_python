from DispositivoEntrada import DispositivoEntrada

class Teclado(DispositivoEntrada):
    contador_teclados = 0
    
    def __init__(self, tipoEntrada, marca) -> None:
        super().__init__(tipoEntrada, marca)
        self.__id_teclado = Teclado.obtener_id()

    
    @classmethod
    def obtener_id(cls):
        cls.contador_teclados += 1
        return cls.contador_teclados
    
    @property
    def id_teclado(self):
        return self.__id_teclado
    
    def __str__(self) -> str:
        return f'Teclado: Id: {self.__id_teclado}, {super().__str__()}'
    

