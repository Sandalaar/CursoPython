#*** IDENTIFICA LA ESTACIÓN DEL AÑO ***
#'''Se solicita proporcionar el valor de un mes (valor númerico entre 1 y 12), e indicar la estación del año según lo siguiente:
# Meses 1, 2, o 12 -> Invierno
# Meses 3, 4 o 5 -> Primavera
# Meses 6, 7 u 9 -> Verano
# Meses 9, 10 u 11 -> Otoño
# Cualquier otro valor -> Estación Desconocida'''
print('*** Estación del Año ***')
mes = int(input('Indica el mes del año usando números, del 1 al 12'))
# Revisión del mes proporcionado
if mes:
    1, 2, 12 = 'Invierno'
elif mes:
    3, 4, 5 = 'Primavera'
elif mes:
    6, 7, 8 = 'Verano'
elif mes:
    9, 10, 11 = 'Otoño'
else:
    'Estación Desconocida'
print('')

# *** Solución Profesor ***
mes = int(input('Proporciona el valor del mes (1-12): '))
estacion = 'Estación desconocida'
# Revisión del mes proporcionado
if mes == 1 or mes == 2 or mes == 12:
    estacion = 'Invierno'
elif mes == 3 or mes == 4 or mes == 5:
    estacion = 'Primavera'
elif mes == 6 or mes == 7 or mes == 8:
    estacion = 'Verano'
elif mes == 9 or mes == 10 or mes == 11:
    estacion = 'Otoño'
else:
    estacion = 'Estacion desconocida'
#imprimimos el resultado
print(f'La estación para el mes {mes} es {estacion}')