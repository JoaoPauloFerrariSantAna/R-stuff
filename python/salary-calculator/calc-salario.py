# qual o próposito da variável "c"???

horas_trabalhadas	= float(input("Quantas horas você trabalhou? "))
horas_excedentes	= 50

ganho_hora			= 10
ganho_excedente		= 20

salario_total		= ganho_hora * horas_trabalhadas

# para saber quantas horas a mais o empregado trabalhou
excesso_hora		= horas_trabalhadas - horas_excedentes
salario_excedente	= ganho_excedente * excesso_hora

if(horas_trabalhadas > horas_excedentes):
	# o "salario_total" tem que ser alterado aqui, pois, 
	# agora que o empregado recebeu mais, ou seja, o salario total dele aumentou
	salario_total = salario_total + salario_excedente

	print(f"Salario total: {salario_total}.")
	print(f"Bonus de horas tranbalhadas: {salario_excedente}.")
	print(f"Horas extras trabalhadas: {excesso_hora}.")
	print(f"Horas trabalhadas (total): {horas_trabalhadas}.")
else:
	salario_excedente = 0
	excesso_hora = 0

	print(f"Salario total: {salario_total}.")
	print(f"Bonus de horas tranbalhadas: {salario_excedente}.")
	print(f"Horas extras trabalhadas: {excesso_hora}.")
	print(f"Horas trabalhadas: {horas_trabalhadas}.")
