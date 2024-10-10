# Crea un programa para solicitar al usuario que proporcione por consola la siguiente información:
#   Nombre
#   Edad(Como un valor de tipo entero)
#   Pais

print('*** Presentate ***')
nombre = input('Ingresa tu nombre: ')
edad = int(input('Ingresa tu edad: '))
pais = input('Ingresa tu país: ')
#print('Tu nombre es: ', nombre)
#print('Tu edad es: ', edad)
#print('Tu país es: ', pais)

#corrección
print(f'Nombre: {nombre}')
print(f'Edad: {edad}')
print(f'pais: {pais}')