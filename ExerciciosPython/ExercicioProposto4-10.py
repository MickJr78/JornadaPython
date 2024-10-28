# AVALIA O TIPO DE TRIÂNGULO QUE TRÊS INTEIROS FORMAM (EQUILÁTERO, ISÓSCELES OU ESCALENO)

numero1 = int(input('Digite o primeiro valor: '))
numero2 = int(input('Digite o segundo valor: '))
numero3 = int(input('Digite o terceiro valor: '))

print('')

# Verifica se todos os números são maiores que zero
if numero1 <= 0 or numero2 <= 0 or numero3 <= 0:
    print("Nenhum dos números pode ser igual ou menor que zero. Tente novamente.")

else:
    # Verifica se a soma de dois lados é maior que o terceiro para todos os casos
    if (numero1 + numero2 > numero3) and (numero1 + numero3 > numero2) and (numero2 + numero3 > numero1):
        print("Temos um triângulo.")

        # Determina o tipo de triângulo
        if numero1 == numero2 == numero3:
            print("Tipo de triângulo: EQUILÁTERO.")
        elif numero1 == numero2 or numero1 == numero3 or numero2 == numero3:
            print("Tipo de triângulo: ISÓSCELES.")
        else:
            print("Tipo de triângulo: ESCALENO.")
    else:
        print("Não é possível formar um triângulo.")
