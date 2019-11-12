par = 0
impar = 0

while True:
  x = int(input("Digite um número: "))
  if x%2 == 0:
    par += 1
  else:
    impar +=1
  print(par,"números pares")
  print(impar,"números impares")
  print()
