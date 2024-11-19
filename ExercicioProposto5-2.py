# Leia um número N e em seguida exiba na tela todos os números divisíveis
# por 7 entre 1 e N (inclusive)

n = int(input('Digite um número: '))
index = 1

while index <= n:
    if index %7 == 0:
        print(index)
    index += 1

print('Fim do programa.')
