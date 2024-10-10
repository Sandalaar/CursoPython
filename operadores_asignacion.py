# Operadores de Asignación
print('*** Operadores de Asignación ***')
a = 5
print(f'Valor de a: {a}')
b = ' Saludos desde Python'
print(f'Valor de b: {b}')
# Por buenas prácticas, se recomienda no usar una sola letra, si no que palabras completas, ejemplo en lugar de a, seria numero, y en lugar de b, seria cadena

# Crear multiples variables en una sola linea
a, b, c = 10, 'Saludos', 14.5
print(f'Valor de a = {a}, b = {b}, c = {c}')

# Asignar un mismo valor a varias variables
x = y = z = 10 # El valor de 10 se le asigna a la variable z, el valor de z a la variable y, y la variable y a la variable x
print(f'Valor de x = {x}, y = {y}, z = {z}')