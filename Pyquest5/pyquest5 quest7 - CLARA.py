"""Construa um programa que armazene números inteiros em um vetor de 10 posições, calcule o quadrado de cada elemento armazenado neste vetor e armazene o resultado em um outro vetor. Ao final os dados do segundo vetor devem ser exibidos no vídeo."""

listnumint =[]
listnumquad = []
for i in range (0,10):
  listnumint.append(int(input('Digite um número inteiro:')))
  listnumquad.append(listnumint[i]**2)
print('-'*30)
print(f'Lista com os números digitados:\n{listnumint}')
print(' ')
print(f'Lista com os quadrados dos números digitados: \n{listnumquad}')