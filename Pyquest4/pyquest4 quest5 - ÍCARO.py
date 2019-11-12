a1 = 0
a2 = 0
a3 = 0
total = 0
altura = float

while True:
  altura = float(input("Digite o altura da pessoa em metros: "))

  if altura > 1.6:
    a1 += 1
  elif altura == 1.6 and altura < 1.8:
    a2 += 1
  else:
    a3 += 1

  print("Total de pessoas: ",a3+a2+a1)
  print("Total de pessoas menores que 1,60m: ",a1)
  print("Total de pessoas entre 1,60m e 1,80m: ",a2)
  print("Total de pessoas com ou mais de 1,80m: ",a3)
  print()
