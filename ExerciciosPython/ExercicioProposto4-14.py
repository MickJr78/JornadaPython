# CALCULA A COTAÇÃO DE TRÊS MOEDAS ESTRANGEIRAS PARA COMPRA

D = 4.89
E = 5.26
L = 6.17

R = float(input('Olá, digite aqui o valor em reais que deseja converter: ').replace(',','.'))

cambio = input('E para qual moeda deseja converter, D - Dólar, E - Euro ou L - Libras? ')

if cambio == 'D':
    moedaConvertida = R / D
    dString = 'Dólar'
    symbolCurrency = 'US$'
elif cambio == 'E':
    moedaConvertida = R / E
    dString = 'Euro'
    symbolCurrency = '€'
elif cambio == 'L':
    moedaConvertida = R / L
    dString = 'Libras Esterlinas'
    symbolCurrency = '£'
else:
    print('Digite uma moeda válida.')

print('Calculando...')
print('O valor de R${:.2f} convertido para {} equivalem a {}{:.2f}'.format(R,dString,symbolCurrency,moedaConvertida).replace(".", ","))