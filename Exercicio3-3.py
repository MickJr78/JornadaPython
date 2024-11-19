a = float(input('Digite um número: '))
b = float(input('Digite outro número: '))
c = float(input('Digite mais um número: '))

r1 = a + b + c
r2 = a * b * c
r3 = 2 * (a + b) - c
r4 = (a + b + c) / 3
r5 = (2 * b + (3 * c)) / (5 * a)
r6 = (a ** 2) + (b ** 2)

print('Estes são os resultados: ')
print('R1=> ',round(r1,3))
print('R2=> ',round(r2,3))
print('R3=> ',round(r3,3))
print('R4=> ',round(r4,3))
print('R5=> ',round(r5,3))
print('R6=> ',round(r6,3))
