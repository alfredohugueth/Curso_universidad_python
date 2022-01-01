from Empleado import Empleado
from Gerente import Gerente

def imprimir_detalles(objeto): # Los metodos deben ser lo mas genericos posible 
    # print(objeto)
    print(type(objeto))
    # Podemos preguntar si un objeto es una instancia de cierta clase:
    print(objeto.mostrar_detalles())
    if isinstance(objeto, Gerente):
        print(objeto.departamento)

empleado = Empleado('Juan', 5000)
imprimir_detalles(empleado)


gerente = Gerente('Karla', 6000, 'Sistemas')
imprimir_detalles(gerente)