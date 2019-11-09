"""Elabore um programa utilizando vetores para armazenar 10 números e ao final escreva a quantidade de números negativos, positivos e nulos."""

numerospositivos = 0
numerosnegativos = 0
numerosnulos = 0
for i in range (0,10):
  num = int(input('Digite um número inteiro:'))
  if num > 0:
    numerospositivos += 1
  elif num < 0:
    numerosnegativos += 1
  elif num == 0:
    numerosnulos += 1
print('-'*30)
print(f'Numeros negativos: {numerosnegativos}')
print(f'Numeros positivos: {numerospositivos}')
print(f'Numeros nulos: {numerosnulos}')