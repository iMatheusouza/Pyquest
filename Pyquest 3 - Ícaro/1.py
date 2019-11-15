tempo = float(input("Digite o tempo de viagem (horas): "))
velocidade = float(input("Digite a velocidade média do automóvel (Km/h): "))
distancia = tempo*velocidade
litros = distancia/12

print("O veículo viajou a velocidade média de %.2f Km/h por %.1f horas, percorrendo %.1f Km e consumindo %.2f litros de combustível" %(velocidade, tempo, distancia, litros))