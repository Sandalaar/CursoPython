# *** CONCATENACIÓN DE CADENAS ***
cadena1 = "Hola"
cadena2= "Mundo"
concatenacion = cadena1 + ' ' + cadena2 #al usar el + en cadenas, se hace una concatenacion y en numeros se hace una suma.
print(concatenacion)

# Utilizando el metodo str.join
concatenacion = "".join([cadena1, ' ', cadena2])
print(concatenacion)