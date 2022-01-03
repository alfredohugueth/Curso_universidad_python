class Monitor:
    contador_monitores = 0

    def __init__(self, marca, tamaño) -> None:
        self.__id_monitor = Monitor.obtener_id()
        self._marca = marca
        self._tamaño = tamaño

    @classmethod
    def obtener_id(cls):
        cls.contador_monitores += 1
        return cls.contador_monitores
    
    @property
    def marca(self):
        return self._marca
    
    @property
    def tamaño(self):
        return self._tamaño
    
    def __str__(self) -> str:
        return f'Monitor: Id {self.__id_monitor}, marca: {self._marca}, tamaño: {self._tamaño}'
    

    