tabuleiro = [0] * 8

i = int(input("Digite a coluna da peça: ")) - 1
j = int(input("Digite a linha da peça: ")) - 1

for m in range(0, 8):
	tabuleiro[m] = [0] * 8

for m in range(0, 8):
	for n in range(0, 8):
		# Esquerda 
		if(n == (j - 2) or n == (j - 1)):
			# cima
			if(m == (i - 2) and n == (j - 1)):
				tabuleiro[m][n] = 1

			if(m == (i - 1) and n == (j - 2)):
				tabuleiro[m][n] = 1

			# baixo
			if(m == (i + 1) and n == (j - 2)):
				tabuleiro[m][n] = 1

			if(m == (i + 2) and n == (j - 1)):
				tabuleiro[m][n] = 1

		# Direita 
		if(n == (j + 2) or n == (j + 1)):
			if(m == (i - 2) and n == (j + 1)):
				tabuleiro[m][n] = 1

			if(m == (i - 1) and n == (j + 2)):
				tabuleiro[m][n] = 1
			# baixo
			if(m == (i + 2) and n == (j + 1)):
				tabuleiro[m][n] = 1

			if(m == (i + 1) and n == (j + 2)):
				tabuleiro[m][n] = 1


tabuleiro[i][j] = 'C'

for m in range(0, 8):
	for n in range(0, 8):
		print(tabuleiro[m][n], end = ' ')

	print()
