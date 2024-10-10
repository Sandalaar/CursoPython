#Tabla Verdad and
# a | b | a and b
#falso | falso | falso
#falso | verdadero | falso
#verdadero | falso | falso
#verdadero | verdadero | verdadero
print('*** Operador and ***')
condicion1 = False
condicion2 = False
resultado = condicion1 and condicion2
print(f'Resultado {condicion1} and {condicion2}: {resultado}')
condicion2 = True
resultado = condicion1 and condicion2
print(f'Resultado {condicion1} and {condicion2}: {resultado}')
condicion1 = True
resultado = condicion1 and condicion2
print(f'Resultado {condicion1} and {condicion2}: {resultado}')
# Regresa verdadero si ambos valores a evaluar son verdareros, y falso si cualquiera de sus falores es falso.

#Tabla Verdad or
#'''a | b | a or b
# false | false | false
# false | true | true
# true | false | true
# true | true | true'''
print('*** Operador or ***')
condicion1 = False
condicion2 = False
resultado = condicion1 or condicion2
print(f'Resultado {condicion1} or {condicion2}: {resultado}')
condicion2 = True
resultado = condicion1 or condicion2
print(f'Resultado {condicion1} or {condicion2}: {resultado}')
condicion1 = True
resultado = condicion1 or condicion2
print(f'Resultado {condicion1} or {condicion2}: {resultado}')
# Regresa verdadero si cualquiera de los valores a evaluar son verdaderos, solo si ambos son falsos regresara falso

#Tabla Verdad not
#a | not a
#false | true
#true | false
usuario_valido = True
print(f'Invertimos valor: {usuario_valido}')
print(f'Invertimos valor: {not usuario_valido}') #Ahora es False
#Este operador solo invierte el resultado