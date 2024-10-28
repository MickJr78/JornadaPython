# AVALIA SE UM ANO É OU NÃO BISSEXTO

ano = int(input('Digite o ano em questão: '))

if (ano % 4 == 0) and(ano %100 != 0) or (ano % 400 == 0):
    print(f'O ano de {ano} é bissexto.')
else:
    print(f'O ano de {ano} NÃO é bissexto.')