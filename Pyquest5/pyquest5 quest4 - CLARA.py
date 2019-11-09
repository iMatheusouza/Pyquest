"""Construa um programa usando vetores que leia o nome e a
nota de 10 alunos e ao final escreva: a nota média da
turma; o nome e a nota dos alunos com resultados
superiores a nota média da turma."""

nomes = []
notas = []
soma = media = 0
for i in range (0,10):
  nomes.append(str(input('Digite o nome de um aluno:')))
  notas.append(float(input('Digite a nota desse aluno:')))
  soma+=notas[i]
media=soma/10
print('-'*35)
print(f'A média da turma é igual a {media:.2f}')
print('-'*35)
print('Alunos acima da média e suas notas:')
print(' ')
for i in range (0,10):
  if notas[i]>=media:
   print(f'{nomes[i]:10} {notas[i]:.2f}')
   print(' ')
print('-'*35)]
