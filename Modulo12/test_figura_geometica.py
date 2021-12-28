from Cuadrado import Cuadrado
from Rectangulo import Rectangulo

cuadrado_1 = Cuadrado('Azul', 5)

print( cuadrado_1.ancho )
print( cuadrado_1.alto )
print( cuadrado_1.color )
print( cuadrado_1.calcular_area() )
print( cuadrado_1 )


# Es importante saber el orden en el que se llaman las clases padre
# Podemos averiguarlo usando el metodo MRO Methon Resolution Order
# Se utiliza este orden de resolucion, para la busqueda de los metodos
# Es importante recalcar que se usa el primer metodo que se encuentre 
print( Cuadrado.mro() )



####### Rectangulo

rectangulo_1 = Rectangulo(11, 3, 'Azul')

print(f'Calculo area rectangulo: { rectangulo_1.calcular_area() }')
print( rectangulo_1 )
