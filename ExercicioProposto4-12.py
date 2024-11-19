# INFORMA QUAL MÊS DO ANO FOI DIGITADO

mesAno = int(input('Digite o mês do ano de 1 a 12: '))

if mesAno >= 1 and mesAno <= 12:
    if mesAno == 1:
        print('JANEIRO')
    elif mesAno == 2:
        print('FEVEREIRO')
    elif mesAno == 3:
        print('MARÇO')
    elif mesAno == 4:
        print('ABRIL')
    elif mesAno == 5:
        print('MAIO')
    elif mesAno == 6:
        print('JUNHO')
    elif mesAno == 7:
        print('JULHO')
    elif mesAno == 8:
        print('AGOSTO')
    elif mesAno == 9:
        print('SETEMBRO')
    elif mesAno == 10:
        print('OUTUBRO')
    elif mesAno == 11:
        print('NOVEMBRO')
    elif mesAno == 12:
        print('DEZEMBRO')
else:
    print(f"Não existe mês com o número {mesAno}")
