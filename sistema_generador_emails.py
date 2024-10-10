#*** SISTEMA GENERADOR EMAILS ***
#Se solicita crear un sistema para generar un email según los datos recibidos. Se debe solicitar:
#   Nombre
#   Apellido
#Con estos datos se debe generar un email como sigue:
#Nombre -> Juan -> Convertir a minúsculas
#Apellido -> Perez -> Convertir a minúsculas
#Resultado: juan.perez@miempresa.com
print('***Sistema generador de emails***')
nombre = input('¿Cual es tu nombre? ')
nombre2 = nombre.lower()
apellido = input('¿Cual es tu apellido? ')
apellido2 = apellido.lower()
mail = '@miempresa.com'
correo = f'{nombre2}.{apellido2}{mail}'
print(f'Tu correo es: {correo}')

#Solución profesor
print('*** Sistema Generador de Emails ***')
nombre = input('Cual es tu nombre? ')
apellido = input('Cual es tu apellido? ')
email_generado = f'{nombre.lower()}.{apellido.lower()}@miempresa.com'
print(f'''
Tu nuevo email generado por el sistema es:
    {email_generado}
    Felicidades!''')