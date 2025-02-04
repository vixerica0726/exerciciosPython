# Programa que calcula o consumo médio de combustível
litros = float(input("Digite a quantidade de litros consumidos: "))
distancia = float(input("Digite a distância percorrida (km): "))

consumo_medio = distancia / litros if litros != 0 else "Indefinido"
print(f"Consumo médio: {consumo_medio} km/l")
