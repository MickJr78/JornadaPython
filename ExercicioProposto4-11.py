# FAZ O CÁLCULO DE MARGEM BRUTA DO PREÇO DE UM PRODUTO

print('Olá, vamos fazer aqui o cálculo da Margem Bruta de um produto.')
precoCustoProduto = float(input('Qual o custo do produto adquirido? ').replace(",", "."))
print('')

print('Aguarde, calculando...')

if precoCustoProduto <= 100.00:
    precoVendaProduto = precoCustoProduto + (precoCustoProduto * 0.45)
    margemAplicada = '45%'
else:
    precoVendaProduto = precoCustoProduto + (precoCustoProduto * 0.35)
    margemAplicada = '35%'

print('Concluído.')

print('VALOR DE CUSTO DO PRODUTO: R${:.2f}'.format(precoCustoProduto).replace(".",","))
print(f'MARGEM APLICADA NO PREÇO DE CUSTO: {margemAplicada}')
print('VALOR DE VENDA DO PRODUTO: R${:.2f}'.format(precoVendaProduto).replace(".",","))
