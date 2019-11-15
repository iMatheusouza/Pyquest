""""Elabore um programa que leia diversos números e ao final
escreva: a quantidade de números digitados, a quantidade de
números pares, a quantidade de números ímpares."""

numeros = 0
pares = 0
impares = 0
while True:
  num = int(input('Digite um número:'))
  numeros += 1
  if num % 2 == 0:
    pares += 1
  else:
    impares += 1
  contresp = str(input('Quer continuar? [S/N]')).strip()
  if contresp in 'Nn':
    break
print(f'Foram digitados {numeros} números: {pares} pares e {impares} ímpares')