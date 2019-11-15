""""Faça um programa que leia o preço de 10 produtos. Ao final
escreva o somatório dos preços.""""

preços = []
soma = 0
for i in range (0,10):
  preços.append(float(input('Digite o preço de um produto:')))
for i in range (0,10):
  soma = soma + preços[i]
print(f'A soma dos preços é igual a R${soma:.2f}')
