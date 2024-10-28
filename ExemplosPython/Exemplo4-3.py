
PH = float(input('Digite o valor do PH: '))

if PH < 6.0:
    r = 'Ácida'
elif PH < 7.0:
    r = 'Levemente ácida'
elif PH == 7.0:
    r = 'Neutra'
elif PH < 8.0:
    r = 'Levemente alcalina'
else:
    r = 'Alcalina'

print(f'Com PH igual a {PH} a solução é {r}.')