print('*** Revisar si un número es Positivo ***')
#Solicitar número
numero = int(input('Ingresa un número: '))

if numero > 0:
    print(f'Es positivo: {numero}')
elif numero < 0:
    print(f'Es negativo: {numero}')
else:
    print(f'Es cero {numero}')