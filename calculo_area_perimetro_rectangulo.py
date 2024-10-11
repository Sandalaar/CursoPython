#'''Cálculo Area y Perimetro de un Rectángulo
# Se solicita calcular el área y perímetro de un rectángulo y aplicando las siguientes fórmulas:
# base x altura
# area = base * altura
# perimetro = 2 * ( base + altura )'''
print('*** Calculo Area y Perímetro de un Rectángulo ***')
#Mi respuesta
base = float(input('Ingresa la base del rectángulo '))
altura = float(input('Ingresa la altura del rectángulo '))
area = base * altura
perimetro = 2 * (base + altura)
print(f'El area del rectángulo es: {area}')
print(f'El perimetro del rectángulo es: {perimetro}')
#Respuesta ChatGPT
# Cálculo del área y perímetro de un rectángulo

# Solicitar al usuario la base y la altura del rectángulo
base = float(input("Ingresa la base del rectángulo: "))
altura = float(input("Ingresa la altura del rectángulo: "))

# Calcular el área
area = base * altura

# Calcular el perímetro
perimetro = 2 * (base + altura)

# Mostrar los resultados
print(f"El área del rectángulo es: {area}")
print(f"El perímetro del rectángulo es: {perimetro}")