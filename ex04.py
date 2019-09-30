x = 0
y = 0

while True:
  sexo = str(input("Digite o sexo da pessoa (M/F): "))
  if sexo == "M" or sexo == "m":
      x += 1
  elif sexo == "F" or sexo == "f":
      y += 1
  print("Total de pessoas",y+x)
  print("Total de mulheres",y)
  print("Total de homens",x)
  print()
