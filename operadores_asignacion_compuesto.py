print('*** Operadores Asignación Compuestos ***')
a, b = 10, 15
print(f'Valor inicial a: {a}. Valor inicial b: {b}')

# Operador compuesto de suma +=
a += b # a = a + b
print(f'Operador a += b es: {a}')

# Operador compuesto de renta -=
a = 10 # reiniciamos el valor de a
a -= b # a = a - b
print(f'Operador a -= b es: {a}')

# Operador compuesto de multiplicación -=
a = 10 # reiniciamos el valor de a
a *= b
print(f'Operador a *= b es: {a}')

# Operador compuesto de división /=
a = 10 # reiniciamos el valor de a
a /= b
print(f'Operador a/= b es: {a}')