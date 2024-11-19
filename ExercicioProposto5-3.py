# FAZ A LEITURA APENAS DE NÚMEROS QUE ESTEJAM NO INTERVALO ENTRE 100 E 200

while True:
    n = int(input('Digite um número entre 100 e 200: '))
    if n < 100 or n > 200:
        print('Este número não está dentro do intervalo. Digite novamente.')

    else:
        print('O valor digitado foi aceito.')
        break
print('Fim')

