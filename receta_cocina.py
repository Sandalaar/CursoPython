# *** RECETA DE COCINA ***
#Crear un programa para solicitar algunos valores importantes para una receta de cocina.
#Los valores que debe introducir el usuario son:
#   Nombre de la Receta
#   Ingredientes
#   Tiempo de preparación (en minutos)
#   Dificultad ("Fácil, Media, Alta")
#Mandar a imprimir la receta

print('*** Receta de cocina ***')
receta = input('Ingrese el nombre de la receta: ')
ingredientes = input('Ingrese los ingredientes separados por una coma(,): ')
tiempoPreparacion = int(input('Ingrese los minutos necesarios para la preparación: '))
dificultad = input('Indique la dificultad de su receta su receta es "Fácil", "Media", "Alta": ')
print(f'Esta receta es de: {receta}')
print(f'Para su preparación se necesitan los siguientes ingredientes: {ingredientes}')
print(f'Su tiempo de cocción es de : {tiempoPreparacion} minutos')
print(f'Su díficultad se considera: {dificultad}')