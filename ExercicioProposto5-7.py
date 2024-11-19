# SOLICITA QUANTIDADES(em números inteiros) DE PRODUTOS VENDIDOS, AO SER DIGITADO
# ZERO OU UM NEGATIVO, EXIBE A SOMATÓRIA DOS VALORES DIGITADOS, SEM QUE O NEGATIVO
# AFETE A CONTAGEM


quant = 0
totalVendido = 0
while True:
    quant = int(input("Digite a quantidade de produtos vendidos: "))
    if quant <= 0:
        print(f"Total vendido: {totalVendido} unidades.")
        break
    else:
        totalVendido += quant
        print(f"Total vendido: {totalVendido} unidades.")

print("Fim da contagem.")