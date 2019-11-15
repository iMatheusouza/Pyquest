op1 = int(input("Escolha (1 - tesoura, 2 - pedra, 3 - papel): "))
op2 = int(input("Escolha (1 - tesoura, 2 - pedra, 3 - papel): "))

if op1 == 1 and op2 == 2:
  print("Jogador 2 venceu (pedra)")
elif op1 == 2 and op2 == 3:
  print("Jogador 2 venceu (papel)")
elif op1 == 3 and op2 == 1:
  print("Jogador 2 venceu (tesoura)")
elif op1 == 2 and op2 == 1:
  print("Jogador 1 venceu (pedra)")
elif op1 == 3 and op2 == 2:
  print("Jogador 1 venceu (papel)")
elif op1 == 1 and op2 == 3:
  print("Jogador 1 venceu (tesoura)")
else:
  print("Empate")