# Se crea primero la clase que no tiene relacion con ninguna otra

class Producto:
    contador_productos = 0

    def __init__(self, nombre, precio) -> None:
        Producto.contador_productos += 1
        self._id_producto = Producto.contador_productos
        self._nombre = nombre
        self._precio = precio
    
    def __str__(self) -> str:
        return f'Id producto : {self._id_producto}, Nombre: {self._nombre}, Precio: {self._precio}'
    
    @property
    def nombre(self) -> str:
        return self._nombre
    
    @property
    def precio(self) -> float:
        return self._precio

if __name__ == '__main__':
    producto_1 = Producto('Camisa', 2000)
    print(producto_1)

    producto_2 = Producto('Pantalon', 3000)
    print(producto_2)
    
