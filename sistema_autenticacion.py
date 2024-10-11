#*** SISTEMA DE AUTENTICACIÓN ***
#'''Crear un sistema para validar los valores de usuario y password proporcionados.
# Se deben definir dos constantes con los valores validos de usuario y password
# Y el sistema debe comparar los valores validos contra los valores proporcionados
# Se deben considerar 4 casos:
#   1. Usuario y password válidos. Debe imprimir 'Bienvenidos al Sistema'
#   2. Usuario inválido
#   3. Password invlálido
#   4. Usuario y Password inválidos'''
print('*** Sistema de Autenticación ***')
USUARIO = 'admin'
PASSWORD = '123'
usuario = input('Cual es tu usuario? ')
password = input('Cual es tu clave? ')
if usuario.lower() == USUARIO and password == PASSWORD:
    print('Bienvenido al sistema')
elif usuario.lower() != USUARIO and password != PASSWORD:
    print('Usuario y Password inválidos')
elif usuario.lower() != USUARIO:
    print('Usuario inválido')
elif password != PASSWORD:
    print('Password inválido')
else:
    print('Digitos inválidos, reintente...')

# *** Solución Profesor ***
print('*** Sistema de Autenticación ***')

USUARIO_VALIDO = 'admin'
PASSWORD_VALIDO = '123'

usuario = input('Ingresa tu usuario: ')
password = input('Ingresa tu password: ')

if usuario == USUARIO_VALIDO and password == PASSWORD_VALIDO:
    print('Bienvenido al Sistema...')
elif usuario == USUARIO_VALIDO:
    print('Password erroneo, favor de corregirlo!')
elif password == PASSWORD_VALIDO:
    print('Usuario erroneo, favor de corregirlo!')
else:
    print('Usuario y password erroneos, favor de corregirlos!')