"""Elabore um programa que leia a idade de diversas pessoas e ao
final informe: o total de pessoas cadastradas, a porcentagem
de pessoas com idade inferior a 18 anos, a porcentagem de
pessoas com idade igual ou superior a 18 anos."""

pessoas = 0
menos18 = 0
mais18 = 0
while True:
  idade = int(input('Digite a idade de uma pessoa:'))
  pessoas += 1
  if idade >= 18:
    mais18 += 1
  if idade < 18:
    menos18 += 1
  contresp = str(input('Quer continuar? [S/N]')).strip()
  if contresp in 'Nn':
    break
print(f'Número de pessoas: {pessoas}')
print(f'Número de pessoas com menos de 18 anos: {menos18}')
print(f'Número de pessoas mais de 18 anos: {mais18}')
