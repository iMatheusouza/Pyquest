"""Elabore um programa que contenha três vetores de 10 posições A,B e C. O objetivo do programa é armazenar números nos vetores A e B e fazer com que o vetor C receba a soma dos elementos correspondentes de A e B. Ao final o programa deve exibir no vídeo o conteúdo de C."""

A = []
B = []
C = []
for i in range (0,10):
  A.append(int(input('Digite um número para o vetor A:')))
for i in range (0,10):
  B.append(int(input('Digite um número para o vetor B:')))
for i in range (0,10):
  C.append(A[i] + B[i])
print(f'Lista A: {A}\nLista B: {B}\nLista C: {C}')