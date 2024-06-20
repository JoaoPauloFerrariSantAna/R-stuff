# código baseado neste vídeo: https://www.youtube.com/watch?v=aRaS1jGViwo
# e em uma print que foi me dada

numeros_primos	= []
inicio			= 1
limite			= 1000

# um número primo é um número > 1 que não pode ser
# formado por nenhum múltiplo de números menores

for numero_checar in range(inicio, limite + 1):
	divisores = 0

	for numeros_ate_checar in range(1, numero_checar + 1):
		# 1 - multiplo é um número do qual está na tabuada de tal número
		# o que eu estou fazendo aqui é pegando todos os números
		# que vem antes de "numero_checar" e mais a "tabuada" o número a frente dele
		# é necessário porque (supondo que n = 1)... "1 * 2 = 2" e "2 * 1 = 2" 
		# e um número primo só pode ter dois divisores,
		# e "numero_checar + 2" não é valido pois...
		# qual número da tábuada do três dá dois?
		if(numero_checar % numeros_ate_checar == 0):
			divisores = divisores + 1

	# 2 - se um número primo somente pode ter 2 divisores,
	# então... quando sair do primeiro loop, e "divisores" for 1 ou 2,
	# é quase garantido que "numero_checar" seja primo
	if(divisores <= 2):
		numeros_primos.insert(numero_checar, numero_checar);

print(f"Números primos entre {inicio} e {limite}: {numeros_primos}")
