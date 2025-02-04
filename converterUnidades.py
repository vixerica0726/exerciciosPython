# Programa que converte quilômetros para metros, centímetros e milímetros
km = float(input("Digite a quantidade de quilômetros: "))
metros = km * 1000
centimetros = metros * 100
milimetros = centimetros * 10

print(f"{km} km equivalem a {metros} metros, {centimetros} cm e {milimetros} mm.")
