# *** SISTEMA DE ENVÍOS ***
#'''Crea un programa para determinar el costo de envío de un paquete según el destino (nacional o internacional) y el peso del paquete.
# Costo Tarifas
#   Nacional = 10 x kilo
#   Internacional = 20 x kilo
# El programa debe solicitar 2 valores:
#   1. Destino (nacional o internacional)
#   2. Peso (kilogramos) del paquete
# Al final debe imprimir el costo de envío del paquete.'''
print('*** Sistema de Envíos ***')
destino = input('Por favor ingrese su destino (nacional/internacional): ')
peso = int(input('Por favor ingrese el peso de su paquete en kilos'))
nacional = destino
internacional = destino
precio_nacional = peso * 10
precio_internacional = peso * 20
if destino.lower() == nacional:
    print(f'Su total a pagar es: ${precio_nacional}')
elif destino.lower() == internacional:
    print(f'Su total a pagar es: ${precio_internacional}')
else:
    print('Destino o peso incorrectos, por favor reintente...')
#Spoiler, no funciono :(

# *** Solución Profesor
print('*** Sistema de Envíos ***')

# Definimos las tarifas de envío por kilogramo
TARIFA_NACIONAL = 10
TARIFA_INTERNACIONAL = 20

# Solicitamos los valores de destino y peso
destino = input('Ingresa el destino del paquete (nacional o internacional)')
peso = float(input('Ingresa el peso del paquete (en kg)'))

costo_envio = None # Definimos la variable del costo de envío. El valor de None significa ausencia de valor.

# Calculo del costo de envío
if destino.lower() == 'nacional':
    costo_envio = peso * TARIFA_NACIONAL
elif destino.lower() == 'internacional':
    costo_envio = peso * TARIFA_INTERNACIONAL
else:
    print('Destino no válido. Ingresa el valor de nacional o internacional')

# Mostrar el costo de envío sólo si es un valor válido
if costo_envio is not None:
    print(f'El costo de envío del paquete es: ${costo_envio:.2f}')