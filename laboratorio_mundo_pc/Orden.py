from Computadora import Computadora
class Orden:

    contador_ordenes = 0

    def __init__(self, computadoras : list) -> None:
        self._id_orden = Orden.obtener_id()
        self._computadoras = computadoras
    
    @classmethod
    def obtener_id(cls):
        cls.contador_ordenes += 1
        return cls.contador_ordenes
    
    def agregar_computadora(self, computadora : Computadora):
        self._computadoras.append(computadora)
    
    def __str__(self) -> str:
        computadoras_str = ''
        for computadora in self._computadoras:
            computadoras_str += computadora.__str__()
        
        return f'''
            Orden: {self._id_orden}
            Computadoras: {computadoras_str}
        ''' 