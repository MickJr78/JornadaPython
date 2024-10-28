# AVALIA MÉDIA DE NOTAS POR ALUNO
from idlelib.replace import replace

nomeAluno =  input('Digite o nome do Aluno: ')
notaUm = float(input('Digite a PRIMEIRA nota: ').replace(",", "."))
notaDois = float(input('Digite a SEGUNDA nota: ').replace(',','.'))
notaTres = float(input('Digite a TERCEIRA nota: ').replace(',','.'))

media = (notaUm + notaDois + notaTres) / 3

if media >= 7.0:
    resultado = 'APROVADO'
else:
    resultado = 'REPROVADO'

print('')
print(f'Aluno: {nomeAluno}')
print('Média das notas: {:.2f}'.format(media))
print(f'Situação: {resultado}')