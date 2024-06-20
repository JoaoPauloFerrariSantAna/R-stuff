prog_exec = True

total = 0

print("Bem vindo ao simulador de caixa eletrônico, digite '0'.")

while(prog_exec):
	quanti_produto = int(input("Quantidade do produto comprado: "))

	if(quanti_produto == 0):
		print("Saindo...")
		break

	preco_unitario = float(input("Qual é o valor unitario do produto? "))

	sub_total	= quanti_produto * preco_unitario 
	total		= total + sub_total

	print("Sub-total: ", sub_total)

print("Total gasto: ", total)
