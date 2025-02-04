# Programa que compara o tempo de viagem em diferentes meios de transporte
distancia_viagem = float(input("Digite a distância da viagem (km): "))

tempo_aviao = distancia_viagem / 600
tempo_carro = distancia_viagem / 100
tempo_onibus = distancia_viagem / 80

print(f"Tempo de viagem: {distancia_viagem} Km")
print(f"Avião: {tempo_aviao:.2f} horas")
print(f"Carro: {tempo_carro:.2f} horas")
print(f"Ônibus: {tempo_onibus:.2f} horas")
