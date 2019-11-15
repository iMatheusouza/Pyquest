"""Crie um programa que leia o nome e a altura de 10 pessoas e
ao final escreva: a altura média do grupo, o nome e a altura
da pessoa mais alta."""

nomes = []
alturas = []
soma = 0
for i in range (0,10):
  nomes.append(str(input('Digite o nome de uma pessoa:')))
  alturas.append(float(input('Digite a altura dessa pessoa:')))
for i in range (0,10):
  soma += alturas[i]
media = soma/10
print(f'A altura média do grupo é: {media}')
print(f'O nome da pessoa mais alta é {nomes[alturas.index(max(alturas))]} e sua altura é {max(alturas):.2f} metros')
