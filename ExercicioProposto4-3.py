# EXERCÍCIO - AVALIAÇÃO DE CONCESSÃO DE EMPRÉSTIMO
from idlelib.replace import replace

pessoa = input('Seja bem vindo ao JuniorCred! Qual é o seu nome? ')
salario = float(input(f'Olá {pessoa}! Por favor, digite aqui o seu salário para que\npossamos avaliar a disponibilidade de crédito para você: ').replace(',','.'))
quantParcelas = int(input('Certo. E em quantas parcelas você deseja pagar seu empréstimo(Máximo de 24x)? '))
baseCalculoConcessao = salario * (8 / 100)
valorParcelas = ((salario / quantParcelas) + ((salario / quantParcelas) * (7.97 / 100)))

if quantParcelas > 24:
    print(f'{pessoa}, a concessão do empréstimo se restringe ao limite de parcelamento de no máximo 24 vezes...')
else:
    if valorParcelas < baseCalculoConcessao:
        print('Parabéns, {}! Com o salário de {:.2f} dividido em {} vezes, o valor \nsolicitado poderá ser liberado para você!'.format(pessoa, salario, quantParcelas))
        resultado = "APROVADO"
    else:
        print(f'Sinto muito, {pessoa}! Suas parcelas poderão exceder o limite de concessão, e por isso, \ninfelizmente não podemos liberar seu empréstimo. :-(')
        resultado = 'REPROVADO'
print('')
print(f'Valor do salário: {salario}')
print(f'Quantidade de parcelas escolhida: {quantParcelas}')
print('Valor das parcelas proposta: {:.2f}'.format(valorParcelas))
print(f'Situação do empréstimo: {resultado}')
