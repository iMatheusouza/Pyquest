nota1 = float(input("Nota 1 = "))
nota2 = float(input("Nota 2 = "))
media = (nota1+nota2)/2
print("Média",media)

if media >= 7:
  print("Aprovado")
else:
  nota3 = float(input("Nota 3 = "))
  media2 = ((nota3*2) + nota2 + nota1)/3
  if media2 >= 6:
    print("Aprovado")
  else:
    print("Reprovado")