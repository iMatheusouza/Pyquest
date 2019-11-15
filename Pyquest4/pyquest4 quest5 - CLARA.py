"""Crie um programa que leia a altura de um número indeterminado
de pessoas. Ao final o programa deve informar o total de
pessoas cadastradas, a quantidade de pessoas com altura
inferior a 1,60 metros; a quantidade de pessoas com altura
entre 1,60 metros e 1,80 metros e a quantidade de pessoas com
altura superior a 1,80 metros."""

totalp = 0
totalinf160 = 0
total160180 = 0
totalsup180 = 0
while True:
  altura = float(input('Digite a altura de uma pessoa:'))
  totalp += 1
  if altura < 1.60:
    totalinf160 += 1
  if altura >= 1.60 and altura <= 1.80:
    total160180 += 1
  if altura > 1.80:
    totalsup180 += 1
  contresp = str(input('Quer continuar? [S/N]')).strip()
  if contresp in 'Nn':
    break
print(f'Total de pessoas: {totalp}')
print(f'Total de pessoas com altura inferior à 1.60: {totalinf160}')
print(f'Total de pessoas com altura entre 1.60 e 1.80: {total160180}')
print(f'Total de pessoas com altura superior à 1.80: {totalsup180}')