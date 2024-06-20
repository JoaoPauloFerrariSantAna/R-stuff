tabuleiro = [0] * 8

i = int(input("Digite a coluna desejada: "))  - 1
j = int(input("Digite a linha desejadas: ")) - 1

topo_tab = -1

for m in range(0, 8):
	tabuleiro[m] = [0] * 8 

# quadrado
for m in range(0, 8):
	for n in range(0, 8):
		if((m == (i - 1) or m == (i + 1)) and ((n == (j - 1)) or (n == (j + 1)))):
			tabuleiro[m][n] = 1

		if(m == i):
			tabuleiro[m][n] = 1

		if(n == j):
			tabuleiro[m][n] = 1

# diagonal e transversal
for m in range(0, 8):
	for n in range(0, 8):
		if((m - i) == (n - j) or (m - i == -(j - n))):
			tabuleiro[m][n] = 1

		if((n - j) == (i - m)):
			tabuleiro[m][n] = 1
		
tabuleiro[i][j] = 'R'

for m in range(0, 8):
	for n in range(0, 8):
		print(f"{tabuleiro[m][n]:^5}", end = ' ');
	print()
