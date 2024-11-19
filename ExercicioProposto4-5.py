
# AVALIA A OBRIGATORIEDADE DO VOTO

idade = int(input('Por favor digite sua idade: '))

if idade < 16:
    print('Não é um eleitor')
elif idade >= 16 and idade < 18 or idade >= 65:
    print('O voto é facultativo.')
else:
    print('O voto é OBRIGATÓRIO.')

