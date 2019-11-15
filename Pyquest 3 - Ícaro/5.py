salario = float(input("Digite o valor do salário R$: "))
sexo = str(input("Digite o sexo(M/F): "))
if sexo == "M" or sexo == "m":
  salario *= 0.95
  print("Salário = R$",salario)
elif sexo == "F" or sexo == "f":
  salario *= 0.97  
  print("Salário = R$",salario)