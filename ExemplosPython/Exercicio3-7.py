# Programa que avalia o retorno de investimentos(ROI)


investimento = float(input('Digite o valor do seu investimento: '))
custos = float(input('Digite o valor total dos CUSTOS: '))
receita = float(input('Digite o valor bruto de ENTRADAS: '))

ROI = ((receita - (custos + investimento)) / (custos + investimento)) * 100

print(f'O valor do ROI total é de {ROI:.1f}%.')
