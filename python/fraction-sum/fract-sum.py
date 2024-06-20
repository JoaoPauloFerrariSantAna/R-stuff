soma		= 1 + (1 / 2) + (1 / 3) + (1 / 4) + (1 / 5) + (1 / 6) + (1 / 7)
prog_exec	= True

print("Digite '0' para sair")

while(prog_exec):
	numero = int(input("Digite o número aqui: "))

	if(numero == 0):
		prog_exec = False
	else:
		fracao	= 1 / numero
		soma	= soma + fracao

print("a soma dos números é", soma)
