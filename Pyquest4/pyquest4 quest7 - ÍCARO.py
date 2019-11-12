x = int
maior = 0

while True:
  x = int(input("Digite um número: "))
  if x > maior:
    maior = x
  print("O maior valor é: ",maior)
