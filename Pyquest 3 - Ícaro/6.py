teste1 = float(input("Conteúdo de carbono %: "))
teste2 = int(input("Dureza de Rokwell: "))
teste3 = int(input("Resistência a tração: "))

if teste1 < 7 and teste2 > 50 and teste3 > 80000:
  print("Aço de grau 10")
elif teste1 < 7 and teste2 > 50:
  print("Aço de grau 9")
elif teste1 < 7:
  print("Aço de grau 8")
else:
  print("Aço grau 7")
