from Orden import Orden
from Producto import Producto

producto_1 = Producto('Camisa', 100.00)
producto_2 = Producto('Pantalon', 150.00)
producto_3 = Producto('Calcetines', 30.0)
producto_4 = Producto('Blusa', 200.00)

productos_1 = [ producto_1, producto_2]
productos_2 = [ producto_3, producto_4]

orden_1 = Orden(productos_1)

orden_1.agregar_producto(producto_3)
orden_1.agregar_producto(producto_4)

print(orden_1)
print(f'Total orden 1: {orden_1.calcular_total()}')

orden_2 = Orden(productos_2)
print(orden_2)
print(f'Total Orden 2: {orden_2.calcular_total()}')

