# Manejo de subcadenas
cadena = 'Hola, mundo!' # su indice va del 0 al 11 siendo 12 caracteres, donde 0 es el inicio y -1 el final

# Obtenemos los primeros 5 caracteres: Hola
subcadena1 = cadena[0:4] #[inicio:fin(exclusivo)]
print(subcadena1) #Como se ve en el ejemplo el final es -1, por lo que para indicar Hola que es del 0 al 3, debemos indicar del 0 al 4 para obtener el "Hola"

# Obtener la sub cadena de Mundo
subcadena2 = cadena[6:11]
print(subcadena2)