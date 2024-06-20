tabuleiro = [0] * 8

# eu preciso gerar uma matriz (FEITO)
# preciso agora colocar alguma coisa em uma coluna e linha especifica (FEITO)

for m in range(0, 8):
	tabuleiro[m] = [0] * 8

i = int(input("Digite o número da coluna: "))
j = int(input("Digite o número da linha: "))

for m in range(0, 8):
	for n in range(0, 8):

		if(m == i):
			tabuleiro[m][n] = 1

		if(n == j):
			tabuleiro[m][n] = 1

# para colocar a "peça" no tabuleiro
tabuleiro[i][j] = 'T'

for m in range(0, 8):
	for n in range(0, 8):
		print(tabuleiro[m][n], end = ' ')
	
	print()

