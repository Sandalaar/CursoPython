#*** SISTEMA DE CALIFICACIONES ***
#'''Crear un programa para convertir una calificación númerica (entre 0 y 10) a una letra (De la F a la A)
# Si es mayor o igual a 9 y menor o igual a 10 es una A
# Si es mayor o igual a 8 y menor a 9 es una B
# Si es mayor o igual a 7 y menor a 8 es una C
# Si es mayor o igual a 6 y menor a 7 es una D
# Si es mayor o igual a 0 y menor a 6 es una F
# En otro caso, imprimir:
#   "Valor Desconocido"'''
print('*** Sistema de Calificaciones ***')
calificacion = int(input('Ingresa la calificación (0-10): '))

if calificacion >= 9 or calificacion == 10:
    print('Tienes una A')
elif calificacion >= 8 and calificacion < 9:
    print('Tienes una B')
elif calificacion >= 7 and calificacion < 8:
    print('Tienes una C')
elif calificacion >= 6 and calificacion < 7:
    print('Tienes una D')
elif calificacion >= 0 and calificacion < 6:
    print('Tienes una F')
else:
    print('Valor Desconocido')

# *** Solución Profesor ***
print('*** Sistema de Calificaciones ***')
calificacion = float(input('Proporciona una calificación entre 0 y 10: '))
calificacion_letra = ''
# Revisamos si esta en los siguientes rangos
if 9 <= calificacion <= 10:
    calificacion_letra ='A'
elif 8 <= calificacion < 9:
    calificacion_letra = 'B'
elif 7 <= calificacion < 8:
    calificacion_letra = 'C'
elif 6 <= calificacion < 7:
    calificacion_letra = 'D'
elif 0 <= calificacion < 6:
    calificacion_letra = 'F'
else:
    calificacion_letra = 'Calificacion incorrecta'
# Imprimimos el resultado
print(f'Calificación {calificacion} es equivalente a {calificacion_letra}')