# Programa que calcula o salário mensal com base no valor por hora trabalhada
salario_hora = float(input("Quanto você ganha por hora? "))
horas_mes = float(input("Quantas horas trabalha no mês? "))

salario_total = salario_hora * horas_mes
print(f"Seu salário mensal é R$ {salario_total:.2f}")
