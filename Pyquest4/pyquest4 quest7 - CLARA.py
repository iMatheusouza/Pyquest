"""Faça um programa que leia vários números inteiros e ao final
escreva o maior."""

numeros = []
while True:
  numeros.append(int(input('Digite um número inteiro:')))
  contresp = str(input('Quer continuar? [S/N]')).strip()
  if contresp in 'Nn':
    break
print(f'O maior número é {max(numeros)}')
