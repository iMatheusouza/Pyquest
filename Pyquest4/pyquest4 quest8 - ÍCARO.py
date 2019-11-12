total = 0
armazenaAlt = 0

for i in range(0,9):
  nome = str(input("Digite o nome: "))
  altura = float(input("Digite a altura da pessoa: "))
  total += altura

  if altura > armazenaAlt:
    armazenaAlt = altura
    armazenaNome = nome

print("Altura média de %.2f metros " %(total/10))
print("%s é @ mais alt@ com %.2f metros de altura:" %(armazenaNome, armazenaAlt))
