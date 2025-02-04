# Programa que calcula o total de calorias queimadas em um mês
horas_semana = float(input("Quantas horas de exercício faz por semana? "))

minutos_mes = horas_semana * 60 * 4
calorias_queimadas = minutos_mes * 5

print(f"Você queima aproximadamente {calorias_queimadas} calorias por mês.")
