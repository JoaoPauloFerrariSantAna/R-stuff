numero = 329

centena = numero // 100
dezena	= (numero % 100) // 10
unidade = numero % 10

if((centena < dezena) and (dezena < unidade)):
	print("O número", numero, "é ascendente")
else:
	print("O número", numero, "não é ascendente")
