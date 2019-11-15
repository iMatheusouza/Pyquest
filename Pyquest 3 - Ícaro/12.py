salario = float(input("Salário R$: "))
inss = salario*0.10
ir = salario*0.25
sindicato = salario*0.005
sb = salario - (inss + ir + sindicato)

print("INSS R$",inss)
print("IR R$",ir)
print("Sindicato R$",sindicato)
print("Salário bruto R$", sb)