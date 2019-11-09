"""Faça um programa usando vetores que armazene o código, o
nome e o telefone de 100 pessoas. O programa deve permitir
que o usuário faça uma consulta dos dados de uma pessoa a
partir de seu código. Esta consulta pode ser repetida se o
usuário desejar, caso contrário, o programa deve ser
encerrado."""

codigos = []
nomes = []
telefones = []
for i in range (0,100):
  codigos.append(int(input('Digite o código dessa pessoa:')))
  nomes.append(str(input('Digite o nome de uma pessoa:')))
  telefones.append(int(input('Digite o telefone dessa pessoa:')))
while True:
  consultresp = str(input('Você quer consultar os dados de uma pessoa? [S/N]'))
  if consultresp not in 'SsNn':
    print('Resposta inválida. Tente novamente (usando S para SIM e N para NÃO):')
  if consultresp in 'nN':
    print('Fim do programa')
    break
  if consultresp in 'sS':
    cod = int(input('Digite o código da pessoa:'))
    if cod in codigos:
      posicao = codigos.index(cod)
      print('Nome:', nomes[posicao])
      print('Telefone:',telefones[posicao])
    if cod not in codigos:
      print('Código invalido. Tente outra vez:')