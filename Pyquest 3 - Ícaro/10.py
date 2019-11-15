h = float(input("Altura(m): "))
sexo = str(input("Digite o sexo(M/F): "))

if sexo == "m" or "M":
  pesoideal = (h*72.7)-58
  print(pesoideal,"Kg")
elif sexo == "f" or "F":
  pesoideal = (h*62.1)-44.7
  print(pesoideal,"Kg")