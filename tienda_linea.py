#'''Tienda en Línea
# Crear un sistema que ofrezca descuentos dependiendo del monto de la compra, o si es miembro de la tienda.
# Se deben revisar las siguientes condiciones:
# Si ha comprado más de $1,000 y es miembro -> Descuento de 10%
# Si sólo es miembro de la tienda -> Descuentro del 5%
# Si no es miembro ni compro más de $1,000 -> Descuento del 0%'''

# *** Mi resultado ***
print('*** Tienda en Línea ***')
monto_compra = float(input('Ingrese el monto de la compra '))
miembro_tienda = input('Es miembro de la tienda (Si/No)? ')

aplica_descuento_10 = monto_compra >= 1000 and miembro_tienda.lower() == "si"
aplica_descuento_5 = miembro_tienda.lower() == "si"

if aplica_descuento_10:
    print(f'Aplica descuento del 10% {aplica_descuento_10} ')
elif aplica_descuento_5:
    print(f'Aplica descuento del 5% {aplica_descuento_5} ')
else:
    print(f'No aplica descuento')

# *** Resultado profesor ***

# Condiciones
MONTO_COMPRA_DESC = 1000

monto_compra = float(input('Cual fue el monto de tu compra? '))
es_miembro = input('Eres miembro de la tienda (si/no)? ')

descuento = 0
# Verificar los datos del cliente
if monto_compra >= MONTO_COMPRA_DESC and es_miembro.lower() == 'si':
    descuento = 0.1 # Descuento del 10%
elif es_miembro.lower() == 'si':
    descuento = .05 # Descuento del 5%
else:
    descuento = 0

# Hacemos los calculos respectivos
if descuento != 0:
    monto_descuento = monto_compra * descuento
    monto_final = monto_compra - monto_descuento
    print(f'\nFelicidades, has obtenido un descuento del {descuento * 100}%')
    print(f'Monto de la compra: ${monto_compra}')
    print(f'Monto de la compra con descuento: ${monto_final}')
else:
    print(f'No se obtuvo ningún tipo de descuento')
    print(f'Te invitamos a hacerte miembro de la tienda')
    print(f'Monto de la compra: ${monto_compra}')