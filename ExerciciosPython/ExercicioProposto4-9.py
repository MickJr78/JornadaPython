# AVALIA A IGUALDADE DE TRÊS NÚMEROS

primeiroNumero =  int(input('Digite um número inteiro: '))
segundoNumero =  int(input('Digite outro número inteiro: '))
terceiroNumero =  int(input('Digite mais um número inteiro: '))
print('')

if primeiroNumero == segundoNumero == terceiroNumero:
    print('Os três valores são iguais.')
elif (primeiroNumero == segundoNumero != terceiroNumero):
    print('Há dois valores iguais e um diferente.')
    print('O primeiro número ', primeiroNumero,' é igual ao segundo, ', segundoNumero, ', e o terceiro é diferente, ', terceiroNumero)
elif(primeiroNumero != segundoNumero == terceiroNumero):
    print('Há dois valores iguais e um diferente.')
    print('O primeiro número ', primeiroNumero, ' é diferente, e o segundo é igual ao terceiro, ', terceiroNumero)
elif(primeiroNumero != segundoNumero) and (primeiroNumero == terceiroNumero):
    print('Há dois valores iguais e um diferente.')
    print('O primeiro número ', primeiroNumero, ' é diferente do segundo, ', segundoNumero, ', mas é igual ao terceiro, ', terceiroNumero)
else:
    print('Os três valores são diferentes.')