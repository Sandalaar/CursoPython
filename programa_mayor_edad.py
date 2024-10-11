#*** PROGRAMA MAYOR EDAD ***
#'''Crea un programa para saber si una persona es mayor de edad.
# Utiliza una constante para indicar el valor cuando una persona se considera mayor de edad.
# Una persona se considera mayor de edad si ha cumplido 18 años.
# Si es mayor de edad debe imprimir:
#   La persona con x años es mayor de edad
# Si es menor de edad debe imprimir:
#   La persona con x años es menor de edad'''
print('Programa Mayor de Edad')
MAYOR_EDAD = 18
edad = int(input('Cual es tu edad? '))
if edad >= 18:
    print(f'La persona con {edad} es mayor de edad.')
else:
    print(f'La persona con {edad} es menor de edad.')

# *** Solución Profesor ***
print('*** Mayor de Edad ***')
MAYOR_EDAD = 18
edad = int(input('Ingresa tu edad: '))

# Validar el valor de edad proporcionado
if edad >= MAYOR_EDAD:
    print(f'La persona con {edad} es mayor de edad')
else:
    print(f'La persona con {edad} es menor de edad')