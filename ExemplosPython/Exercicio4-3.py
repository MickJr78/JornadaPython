a = int(input('Digite o valor de A: '))
b = int(input('Digite o valor de B: '))

#
# if a == b:
#     print(f'Os dois números são iguais e valem {a}.')
# else:
#     if a < b:
#         print(f'O menor número é {a}')
#     else:
#         print(f'O menor número é {b}')
#
# print('Fim do programa.')


# AQUI TAMBÉM VALE USAR A CONSTRUÇÃO 'ELIF', QUE SEGUE A MESMA
# INDENTAÇÃO DO CÓDIGO INICIAL, SEM ANINHAMENTO.


if a == b:
    print(f'Os dois números são iguais e valem {a}.')
elif a < b:
    print(f'O menor número é {a}')
else:
    print(f'O menor número é {b}')

print('Fim do programa.')
