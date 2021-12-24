edadAdulto = 18
edadPersona = int(input('Proporciona tu edad: '))

if edadPersona >= edadAdulto:
    print(f'La edad de la persona {edadPersona} es un adulto')
else:
    print(f'La edad de la persona {edadPersona} es menor de edad')
