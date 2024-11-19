# SOLICITA QUE O USUÁRIO DIGITE DOIS NÚMEROS, UM PARA UMA FAIXA MÍNIMA
# E OUTRO PARA A FAIXA MÁXIMA, ENTÃO EXIBE UMA FAIXA NUMÉRICA DENTRO DO INTERVALO
# DOS DOIS NÚMEROS DIGITADOS.

LMin = int(input("Digite um valor inicial de faixa mínima: "))
LMax = int(input("Digite um valor final de faixa máxima: "))

while LMin <= LMax:
    print(LMin, end=" -> ")
    LMin += 1

print("Fim da Contagem.")