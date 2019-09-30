tempo = 0

massa = float(input("Digite o valor da massa inicial em gramas(g): "))
while massa > 0.5:
  massa = massa/2
  tempo += 50
print("Após %i segundos a massa final é de %.2f" %(tempo, massa))
