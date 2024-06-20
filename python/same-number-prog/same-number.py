# melhores nomes
for numero in range(1000, 9999):
		primeira_parte = numero // 100
		segunda_parte = numero % 100

		numeros_somados = primeira_parte + segunda_parte
		numero_elevado = numeros_somados ** 2

		if(numero_elevado == numero):
			print(f"({primeira_parte} + {segunda_parte})^2 = {numero}")
