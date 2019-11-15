"""Faça um programa que leia a idade de 10 pessoas. Ao final
escreva a média das idades."""

idades = []
soma = 0
for i in range (0,10):
  idades.append(int(input('Digite a idade de uma pessoa:')))
for i in range (0,10):
  soma += idades[i]
media = soma/10
print(f'A média das idades dessas pessoas é igual a {media}')