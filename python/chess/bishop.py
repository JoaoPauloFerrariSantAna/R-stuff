tabuleiro = [0] * 8

for m in range(0, 8):
	tabuleiro[m] = [0] * 8

i = int(input("Digite a coluna: ")) - 1
j = int(input("Digite a linha: ")) - 1

for coluna in range(0, 8):
	for linha in range(0, 8):
		# diagonal
		if((coluna - i) == (linha - j) or (coluna - i == -(j - linha))):
			tabuleiro[coluna][linha] = 1

		# transversal
		if((linha - j) == (i - coluna)):
			tabuleiro[coluna][linha] = 1
			

tabuleiro[i][j] = 'B'

for m in range(0, 8):
	for n in range(0, 8):
		print(tabuleiro[m][n], end = ' ')
	print()
