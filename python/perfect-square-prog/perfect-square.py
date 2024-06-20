numero_checar = int(input("Digite um número para ver se ele é um quadrado perfeito: "))

soma = 0
i = 0

while(soma <= numero_checar):
	if(i % 2 != 0):
		soma = soma + i

		# eu não consegui fazer só uma mensagem aparecer,
		# sempre vai ficar alternando entre "(tal numero) não é um quadrado perfeito
		# e "(tal número) é um quadrado perfeito
		if(soma != numero_checar):
			print(f"{numero_checar} não é um quadrado perfeito")
		else:
			print(f"{numero_checar} é um quadrado perfeito")

	i = i + 1
