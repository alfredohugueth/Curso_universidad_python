class Aritmetica:

    """
    Clase Aritmetica para realizar las operaciones de sumar, restar, etc
    """

    def __init__(self, operandoA, operandoB) -> None:
        self.operandoA = operandoA
        self.operandoB = operandoB
    
    
    def sumar(self) -> int:
        return self.operandoA + self.operandoB
    
    def restar(self) -> int:
        return self.operandoA - self.operandoB
    
    def multiplicar(self) -> int:
        return self.operandoA * self.operandoB
    
    def division(self) -> float:
        return self.operandoA / self.operandoB
    
    


arimetica_1 = Aritmetica(5,4)
print(f'Suma: {arimetica_1.sumar()}')

print(f'Resta: {arimetica_1.restar()}')

print(f'Multiplicacion: {arimetica_1.multiplicar()}')

print(f'Division: {arimetica_1.division():.2f}') # El :.2f me permite imprimir la cantidad de puntos flotantes deseados 
