from Producto import Producto
class Orden:
    contador_ordenes = 0

    def __init__(self, productos) -> None:
        Orden.contador_ordenes += 1
        self._id_orden = Orden.contador_ordenes
        self._productos = list(productos) # Si es una lista, pasa la verificacion, en caso contrario, da error

    def agregar_producto(self, producto):
        self._productos.append(producto)
    
    def calcular_total(self):
        total = 0
        
        for producto in self._productos:
            total += producto.precio
        
        return total
    
    def __str__(self) -> str:
        productos_str = ''
        for producto in self._productos:
            productos_str += producto.__str__() + '|'
        
        return f'Orden: {self._id_orden}, Productos: {productos_str}'
    

if __name__ == '__main__':
    producto_1 = Producto('Camisa', 100.00)
    producto_2 = Producto('Pantalon', 150.00)
    productos = [ producto_1, producto_2] # Lista de productos

    orden_1 = Orden(productos)

    print(orden_1)