"""Elabore um programa que leia a matrícula e o salário bruto
de 100 empregados. Os dados devem ser armazenados em
vetores. O programa deve descontar 11% do salário bruto de
cada empregado e ao final escrever: a matrícula, o salário
bruto, o desconto e o salário líquido de cada empregado."""

matriculas = []
salariosbrutos = []
salariosliquidos = []
descontos = []
for i in range (0,100):
  matriculas.append(int(input('Digite a matrícula de um empregado: ')))
  salariosbrutos.append(float(input('Digite o salário bruto desse empregado: ')))
  descontos.append(salariosbrutos[i] * (11/100))
  salariosliquidos.append(salariosbrutos[i] - descontos[i])
print('-'*35)
for i in range (0,100):
  print(' ')
  print(f'O funcionário com a matrícula {matriculas[i]} teve o salário bruto de R${salariosbrutos[i]:.2f}, do qual foi descontado R${descontos[i]:.2f}, sobrando assim um salário líquido de R${salariosliquidos[i]:.2f}')