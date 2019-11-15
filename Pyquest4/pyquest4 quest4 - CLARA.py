"""Elabore um programa que leia o sexo de um número
indeterminado de pessoas. Ao final escreva a quantidade de
pessoas cadastradas e o total de pessoas de cada sexo."""

totalF = 0
totalM = 0
total = 0
while True:
  sexo = str(input('Insira o sexo de uma pessoa [F/M]:')).strip()
  if sexo not in 'FfMm':
    print('Sexo inválido.')
  if sexo in 'FfMm':
    total +=1
  if sexo in 'Ff':
    totalF += 1
  if sexo in 'Mm':
    totalM += 1
  contresp = str(input('Quer continuar? [S/N]')).strip()
  if contresp in 'Nn':
    break
print(f'O total de pessoas é igual a {total}')
print(f'O total de pessoas do sexo feminino é igual a {totalF}')
print(f'O total de pessoas do sexo masculino é igual a {totalM}')
