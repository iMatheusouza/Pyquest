"""Faça um programa utilizando vetores que leia 10 números inteiros e ao final escreva estes números na ordem crescente e na ordem decrescente."""

numeros = []
for i in range (0,10):
  numeros.append(int(input('Digite um número inteiro:')))
print('-'*30)
print(f'Lista desses números organizados de forma crescente: {sorted(numeros)}')
print(' ')
print(f'Lista desses números organizados de forma decrescente: {sorted(numeros, reverse=True)}')
