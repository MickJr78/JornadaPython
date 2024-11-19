# FAZ UM LOOP CONTÍNUO ENQUANTO O VALOR DIGITADO NÃO FOR ZERO, DEPOIS SOMA
# TUDO QUE FOI DIGITADO

soma = qtde = 0
A = 1
while A != 0:
    A = int(input("Digite X: "))
    soma = soma + A
    qtde = qtde + 1
print(f'Soma dos valores = {soma}')
