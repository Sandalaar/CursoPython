#*** EL MAYOR DE DOS NÚMEROS ***
#'''Crear un programa para indicar cual es el mayor de dos números.
#El programa debe pedir al usuario dos números enteros.
# Posteriormente se deben comparar y mandar a imprimir el número mayor.'''
print('*** El Mayor de 2 Números ***')

numero1 = int(input('Ingrese el primer número: '))
numero2 = int(input('Ingrese el segundo número: '))

# El mayor de dos números
if numero1 > numero2:
    print(f'El primer número es mayor: {numero1}')
else:
    print(f'El segundo número es mayor: {numero2}')

# El mayor de dos números, pero usando el OPERADOR TERNARIO.
resultado = "Número 1 es mayor" if numero1 > numero2 else "Número 2 es mayor"
print(f'El mayor de los dos números es: {resultado}')