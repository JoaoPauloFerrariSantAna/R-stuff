# código baseado neste vídeo: https://www.youtube.com/watch?v=aRaS1jGViwo
# e em uma print que foi me dada

numeros_primos	= []
quanti_primos	= 0
inicio			= 1
numero_proc		= int(input("Digite um número: "))

for numero_checar in range(inicio, numero_proc + 1):
	divisores = 0

	# 1 - multiplo é um número do qual está na tabuada de tal número
	# o que eu estou fazendo aqui é pegando todos os números
	# que vem antes de "numero_checar" e mais a "tabuada" o número a frente dele
	# é necessário porque (supondo que n = 1)... "1 * 2 = 2" e "2 * 1 = 2" 
	# e um número primo só pode ter dois divisores,
	# e "numero_checar + 2" não é valido pois...
	# qual número da tábuada do três dá dois?
	for numeros_ate_checar in range(inicio, numero_checar + 1):
		if(numero_checar % numeros_ate_checar == 0):
			divisores = divisores + 1

	# 2 - se um número primo somente pode ter 2 divisores,
	# então... quando sair do primeiro loop, e "divisores" for 1 ou 2,
	# é quase garantido que "numero_checar" seja primo
	if(divisores <= 2):
		numeros_primos.insert(numero_checar, numero_checar);
		quanti_primos = quanti_primos + 1


# porque o comprimento da lista é diferente da quantidade de itens
# que eu tenho (de 1 a 100 é 25 itens, mas 0 é incluido, então 24)
total_checar = quanti_primos - 1

if(numero_proc == numeros_primos[total_checar]):
	print(f"{numero_proc} já é primo")
else:
	print(f"O número mais próximo de {numero_proc} é {numeros_primos[total_checar]}")
