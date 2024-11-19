salario = 1200.00
nomeVendedor =  input('Digite o nome do vendedor: ')
valorVendas = float(input('Digite o valor vendido neste mês: '))
comissao = valorVendas * 0.06
totalRecebido = round(salario + comissao, 2)
print(f'Vendedor {nomeVendedor} vendeu R${valorVendas} e faz jus a uma comissão de R${totalRecebido}.')