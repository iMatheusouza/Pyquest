"""Faça um programa utilizando vetores que leia o nome e a
altura de 50 pessoas e ao final escreva o nome e a altura
das pessoas com mais de 1,70 metros."""

nomes=[]
alturas=[]
for i in range (0,3):
  nomes.append(str(input('Digite o nome: ')))
  alturas.append(float(input('Digite a altura: ')))
print('-'*35)
print("Pessoas maiores que 1,70 metros:")
for i in range(len(alturas)):
  if alturas[i]>1.70:
    print(' ')
    print(f'Nome: {nomes[i]}\nAltura: {alturas[i]:.2f} metros')