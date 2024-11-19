#AVALIA CLASSIFICAÇÃO INDICATIVA

classIndicativa = 16

idade = int(input('Olá, digite a sua idade: '))

if idade < classIndicativa:
    print('Sinto muito, você não pode assistir a este filme.')
else:
    print(f'Seja bem vindo! Com {idade} anos você está liberado para assistir este filme. Bom divertimento!')