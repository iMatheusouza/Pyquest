salario = float(input("Salário: "))
if salario < 2000:
  gratificacao = "Gratificação 5%"
  salario += salario*0.05
  print(gratificacao)
  print("Salário R$:",salario)
elif salario >= 2000 and salario <= 2500:
  gratificacao = "Gratificação 10%"
  salario += salario*0.1
  print(gratificacao)
  print("Salário R$:",salario)
elif salario > 2500 and salario <= 3000:
  gratificacao = "Gratificação 15%"
  salario += salario*0.15
  print(gratificacao)
  print("Salário R$:",salario)
elif salario > 3000:
  gratificacao = "Gratificação 20%"
  salario += salario*0.2
  print(gratificacao)
  print("Salário R$:",salario)