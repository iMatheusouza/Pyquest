saldo = int(input("Saldo médio R$: "))
if saldo >= 0 and saldo <= 200:
  print("Nenhum crédito")
elif saldo >= 201 and saldo <= 400:
  print("saldo: %i crédito: %i" %(saldo,(saldo*20)/100))
elif saldo >= 401 and saldo <= 600:
  print("saldo: %i crédito: %i" %(saldo,(saldo*30)/100))
elif saldo > 600:
  print("saldo: %i crédito: %i" %(saldo,(saldo*40)/100))