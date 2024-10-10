#'''***SISTEMA PRÉSTAMO DE LIBROS***
# Se pide crear un sistema para una biblioteca, la cual desea prestar libros si cumple con cualquiera de las siguientes condiciones.
# 1 El usuario tiene credencial de estudiante
# 2 El usuario vive a no más de 3 km a la redonda
# Si cumple con cualquiera de estas condiciones se le puede prestar el libro'''
print('*** Sistema Préstamo de Libros ***')

DISTANCIA_PERMITIDA_KM = 3
tiene_credencial = input('Cuentas con credencial de estudiante (Si/No)? ')
distancia_biblioteca_km = int(input('A cuantos km vives de la biblioteca? '))

es_elegible_prestamo = (tiene_credencial.lower() == 'si' 
                        or distancia_biblioteca_km <= DISTANCIA_PERMITIDA_KM)

print(f'Eres elegible para prestamo de libros? {es_elegible_prestamo}')