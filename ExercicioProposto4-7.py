# AVALIA O INGRESSO NO SERVIÇO MILITAR DE ALBALÂNDIA

print('Seja bem vindo ao Programa de Ingresso no Serviço Militar de Albalândia! Juntos somos mais fortes!')
nome = input('Primeiro, digite o seu nome: ')
idade = int(input('Agora, digite a sua idade: '))
sexo = input("Por fim, digite o seu sexo com apenas 1 caracter('m' / 'M' para masculino \nou 'f' / 'F' para feminino):")

if (sexo != 'f' and sexo != 'F') and (sexo != 'm' and sexo != 'M'):
    print('')
    print('Descrição de sexo incorreta. Por favor tente novamente.')
else:
    if (sexo == 'f' or sexo == 'F') and (idade >= 21 and idade <= 34):
        resultado = 'ACEITO(A)'
    elif  (sexo == 'm' or sexo == 'M') and (idade >= 18 and idade <= 39):
        resultado = 'ACEITO(A)'
    else:
        resultado = 'DISPENSADO DA PRESTAÇÃO DO SERVIÇO MILITAR.'

    print('')
    print(f'Nome do candidato: {nome}')
    print(f'Idade do candidato: {idade}')
    print(f'Status da candidatura: {resultado}')

