# SOLICITA AO USUÁRIO A ENTRADA DE DOIS PADRÕES DE INFORMAÇÃO SOBRE UM PRODUTO
# CASO O USUÁRIO DIGITE UM PADRÃO DIFERENTE DO ESPERADO, EXIBE UMA MENSAGEM DE ERRO.
# AO SER DIGITADO O '0', ENCERRA A EXECUÇÃO DO PROGRAMA.


total1 = 0
total2 = 0
print('Seja bem-vindo!')
while True:
    code = int(input(
        'Digite o código de aplicação do produto, \nsendo (1) para RESIDENCIAL e (2) para industrial. Para encerrar, digite (0): '))
    if code == 1:
        uso = 'RESIDENCIAL'
        quant = int(input('Digite a quantidade vendida: '))
        total1 += quant
    elif code == 2:
        uso = 'INDUSTRIAL'
        quant = int(input('Digite a quantidade vendida: '))
        total2 += quant
    elif code == 0:
        break
    else:
        print('Você digitou um código inválido! Tente novamente.')

print(f'Total de produtos de uso RESIDENCIAL: {total1}')
print(f'Total de produtos de uso INDUSTRIAL: {total2}')
