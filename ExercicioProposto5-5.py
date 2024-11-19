# SEGUE O MESMO OBJETIVO PROPOSTO NO EXERCÍCIO 5.4, COM O DIFERENCIAL QUE SOLICITA UM TERCEIRO
# NÚMERO QUE SERÁ O VALOR QUE SERÁ ACEITO COMO DIVISOR ENTRE TODOS OS NÚMEROS DO INTERVALO.

LMin = int(input("Digite um valor inicial de faixa mínima: "))
LMax = int(input("Digite um valor final de faixa máxima: "))
D = int(input("Agora, digite um número inteiro para ser o divisor: "))
while LMin <= LMax:
    if LMin % D == 0:
        print(LMin, end=" -> ")
    LMin += 1
print("Fim da Contagem.")