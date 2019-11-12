maior = 0
menor = 0
total = int

while True:
  idade = int(input("Digite a idade da pessoa: "))
  if idade < 18 and idade > 0:
      menor += 1
  elif idade > 18:
      maior += 1
  total = menor + maior

  print("Total de pessoas",total)
  print("Total de maiores de idade",(maior/total)*100)
  print("Total de menores de idade",(menor/total)*100)
  print()
