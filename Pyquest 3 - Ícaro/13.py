n1 = float(input("Digite N1: "))
n2 = float(input("Digite N2: "))
n3 = float(input("Digite N3: "))

if n1 == n2 or n1 == n3 or n2 == n3:
  print("Os valores digitados não são diferentes")
elif n1 > n2 and n1 > n3:
  print(n1,"é o maior (N1)")
elif n2 > n1 and n2 > n3:
  print(n2,"é o maior (N2)")
else:
  print(n3,"é o maior (N3)")