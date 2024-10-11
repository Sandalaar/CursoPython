print('*** Sentencias de Decisión Múltiples ***')

dia_con_lluvia = True
dia_nublado = False

if dia_con_lluvia:
    print('Llevar paraguas')
elif dia_nublado:  #es la abreviatura de else if, y se utiliza para enviar a comprobar una segunda condición si la primera condición no se cumple
    print('Llevar impermeable')
#elif condicion 3:
#elif condicion 4:
# Se pueden utilizar cuantos elif se requieran entre el if y el else
else:
    print('Dejar paraguas e impermeable en casa')