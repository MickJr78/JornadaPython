# AVALIA A LINHA DE CALÇADOS POR CÓDIGO

LL = int(input('Entre com o código para saber a qual linha o calçado pertence: '))
print('')

if LL == 16:
    print('Calçados para bebês.')
elif LL == 23:
    print('Calçado infantil feminino.')
elif LL == 25:
    print('Calçado infantil masculino.')
elif LL == 29:
    print('Calçado infantil esportivo.')
elif LL == 42:
    print('Calçado masculino formal.')
elif LL == 43:
    print('Calçado masculino casual.')
elif LL == 49:
    print('Calçado masculino esportivo.')
elif LL == 52:
    print('Calçado feminino formal salto baixo.')
elif LL == 53:
    print('Calçado feminino formal salto alto.')
elif LL == 55:
    print('Calçado feminino casual salto baixo.')
elif LL == 56:
    print('Calçado feminino casual salto alto.')
elif LL == 59:
    print('Calçado feminino esportivo.')
else:
    print('Código Inválido. Verifique o código e entre novamente.')
