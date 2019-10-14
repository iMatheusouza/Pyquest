nome = []
altura = []
tamanho = 50

for i in range (tamanho):
    nome.append(input('Digite seu nome'))
    altura.append(float(input('Digite sua altura')))
    if altura[i] > 1.70:
        print'{} tem mais de 1.70 de altura'.format(nome[i]))