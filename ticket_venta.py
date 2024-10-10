#*** GENERACIÓN TICKET VENTA ***
#'''Supongamos que compramos varios artículos en el supermercado y queremos obtener el ticket de venta total incluyendo impuestos.
# El sistema solicitará el precio de cada producto a comprar y el usuario deberá indicar su precio (valor de tipo con punto decimal)
# El sistema debe realizar la suma de cada producto, calcular el impuesto y finalmente imprimir el total de la compra'''
print('*** Generación Ticket de Venta ***')
precio_leche = float(input('Precio leche: '))
precio_pan = float(input('Precio pan: '))
precio_lechuga = float(input('Precio lechuga:'))
precio_platanos = float(input('Precio platanos: '))

# Calcular el subtotal (sin impuestos)
subtotal = precio_leche + precio_pan + precio_lechuga + precio_platanos

# Calcular el impuesto (16%)
impuesto = subtotal * .16

# Calculo total de la compra (incluyendo impuestos)
costo_total_compra = subtotal + impuesto

# Generar el ticket de venta
print(f'''
Subtotal: ${subtotal}
Impuesto (16%) ${impuesto}
Costo total de la compra: ${costo_total_compra}''')
#puede que de un resultado como por ejemplo 80.77777, para evitar esto podemos darle un formato agregando {subtotal:.2f}, de esta forma dara un resultado como 80.77
print(f'''
Subtotal: ${subtotal:.2f}
Impuesto (16%) ${impuesto:.2f}
Costo total de la compra: ${costo_total_compra:.2f}''')

#podemos agregar descuentos de la siguiente forma:
descuento_porcentaje = int(input('Aplicar algún descuento(%)? '))
#Aplicar el descuento
descuento = subtotal * (descuento_porcentaje/100) #el descuento_porcentaje se divide entre 100, ejemplo si el cliente indica 10% nos dara un 0.1 para aplicar el descuento
#Subtotal con descuento
subtotal_con_descuento = subtotal - descuento
#Calcular el impuesto (16%)
impuesto = subtotal_con_descuento * .16
#Calcular total de la compra (incluyendo impuestos)
costo_total_compra = subtotal_con_descuento + impuesto
print(f'''
--- Ticket de Venta ---
Subtotal: ${subtotal:.2f}
Descuento: ${descuento:.2f} ({descuento_porcentaje}%)
Subtotal con descuento: ${subtotal_con_descuento:.2f}
Impuesto (16%) ${impuesto:.2f}
Costo total de la compra: ${costo_total_compra:.2f}''')