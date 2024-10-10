# *** SISTEMA DESCUENTOS VIP ***
#'''Una tienda de supermercado ofrece un descuento especial a clientes que compren 10 o más artículos por día Y además sean miembros de la tienda
# El sistema debe solicitar al cliente que indique cuántos artículos ha comprado en el día y preguntarle si cuenta con la membresía de la tienda
# En caso de haber comprado 10 o más productos y ser miembro de la tienda entonces tendrá acceso al descuento VIP'''
print('*** Sistema Descuentos VIP ***')
NO_PRODUCTOS_DESCUENTO = 10 #Recordemos que las constantes son en mayúsculas
cantidad_productos = int(input('Cuantos productos compraste hoy?'))
tiene_membresia = input('Cuentas con la membresia de la tienda (Si/No)? ')

es_elegible_descuento = (cantidad_productos >= NO_PRODUCTOS_DESCUENTO 
                        and tiene_membresia.lower() == "si") #envolviendolo en parentesis, podemos darle a enter para bajar una linea manteniendo la misma linea de codigo
#Aunque el () no es necesario si no se quiere bajar de linea

print(f'Tienes acceso al descuento VIP? {es_elegible_descuento}')