"""A conversão de graus Farenheit para graus centígrados é
obtida por : C = 5/9 * (F -32). Faça um programa que calcule
e escreva uma tabela de centígrados em função de graus
Farenheit, que variam de 100 a 150 de 1 em 1."""

for i in range (100,151):
  F = i
  C = 5/9 * (F -32)
  print(f'{F} graus Farenheit = {C:.2f} graus Celsius')
