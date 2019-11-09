"""Faça um programa utilizando vetor que leia 9 números
inteiros. Ao final o programa deve informar o maior
número, a quantidade de vezes que ele ocorre e em quais
posições do vetor."""

numeros = []
posições = []
maior = 0
for i in range (0,9):
  numeros.append(int(input('Digite um número inteiro:')))
print('-'*30)
for i in range (0,9):
  if numeros[i] > maior:
    maior = numeros[i]
for i in range (0,9):
  if numeros[i] == maior:
    posições.append(i)
print(f'O maior número do vetor é {maior}')
print(' ')
print(f'O número {maior} aparece {numeros.count(maior)} vezes')
print(' ')
print(f'O número {maior} aparece nas posições: {posições}')