#'''***Valor Dentro de Rango ***
# Solicitar al usuario un valor entre 0 y 5 e indicarle si el valor proporcionado está dentro de rango.
# Se deben definir 2 constantes, VALOR_MINIMO = 0 y VALOR_MÁXIMO = 5
# Y debemos comprobar si el valor proporcionado se encuentra en el rango entre 0 y 5
# Finalmente se debe imprimir:
# Valor dentro de rango: True/False'''
print('***Valor Dentro de Rango ***')
#Condiciones
MINIMO = 0
MAXIMO = 5

# Solicitamos un valor entre 0 y 5
dato = int(input('Proporcione un dato entre 0 y 5: '))

# Verificamos si estamos dentro de rango
# dentro_rango = dato >= MINIMO and dato <= MAXIMO
dentro_rango = MINIMO <= dato <= MAXIMO #código de linea anterior simplificado
print(f'Valor dentro de rango? {dentro_rango}')