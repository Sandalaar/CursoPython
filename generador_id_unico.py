#Sistema Generador ID Único
#Se solicita crear un sistema para generar un ID único para cada persona.
#El sistema debe solicitar al usuario:
#   Nombre
#   Apellido
#   Año de Nacimiento (YYYY)
print('*** GENERADOR DE ID ÚNICO***')
nombre = input('Ingrese su nombre: ')
apellido = input('Ingrese su apellido: ')
nacimiento = int(input('Ingrese su año de nacimiento: '))
print(f'Su ID ÚNICO es: {nombre[0:3]}{apellido[0:2]}{nacimiento[2:-1]}')

#correcciones:
#Con los datos recibidos el sistema deberá realizar lo siguiente:
#1 Del valor recibido de nombre, usar sólo las 2 primeras letras y convertirlas a mayúsculas
#2 Del valor de apellido, usar las 2 primeras letras y convertirlas a mayúsculas
#3 Del valor de año, tomar los 2 últimos dígitos

#Además el sistema deberá generar un valor aleatorio de 4 dígitos, con ayuda de la función randint
#Finalmente, con los datos obtenidos generar un ID único uniendo los valores como sigue:
#Ej. Nombre -> Juan -> JU
#   Apellido -> Perez -> PE
#   Año Nacimiento -> 1995 -> 95
#   Valor Aleatorio -> randint -> 7326
#   Resultado ID único: JUPE957326

#Resultado ChatGPT:
import random

# Sistema Generador ID Único
# Se solicita crear un sistema para generar un ID único para cada persona.

print('*** GENERADOR DE ID ÚNICO ***')

# Solicitar nombre, apellido y año de nacimiento
nombre = input('Ingrese su nombre: ')
apellido = input('Ingrese su apellido: ')
nacimiento = int(input('Ingrese su año de nacimiento (YYYY): '))

# 1. Usar las primeras 2 letras del nombre y convertirlas a mayúsculas
nombre_id = nombre[0:2].upper()

# 2. Usar las primeras 2 letras del apellido y convertirlas a mayúsculas
apellido_id = apellido[0:2].upper()

# 3. Tomar los últimos 2 dígitos del año de nacimiento
nacimiento_id = str(nacimiento)[-2:]

# Generar un valor aleatorio de 4 dígitos
valor_aleatorio = random.randint(1000, 9999)

# Generar el ID único uniendo todos los valores
id_unico = f'{nombre_id}{apellido_id}{nacimiento_id}{valor_aleatorio}'

# Mostrar el resultado
print(f'Su ID ÚNICO es: {id_unico}')

#Corrección profesor Udemy:
# import random #también puede hacerse como la linea siguiente para importar solo una parte que es la que queremos:
from random import randint
print('*** Sistema Generador de ID Único ***')
nombre = input('Cual es tu nombre? ')
nombre_2 = nombre[0:2].upper()
apellido = input('Cual es tu apellido? ')
apellido_2 = apellido[0:2].upper()
anio_nacimiento = input('Cual es tu año de nacimiento (YYYY)? ') #Y - year
anio_nacimiento_2 = anio_nacimiento[2:4]
# Generar un valor aleatorio de 4 dígitos
aleatorio = randint(1000, 9999)
# Generamos el ID único
id_unico = f'{nombre_2}{apellido_2}{anio_nacimiento_2}{aleatorio}'
print(f'''\nHola {nombre},
    Tú nuevo número de identificación (ID) generado por el sistema es:
    {id_unico}
    Felicidades!''')