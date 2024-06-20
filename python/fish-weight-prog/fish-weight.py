peso_peixe		= float(input("Peso do peixe: "))
peso_permitido	= 50

# porque nós precisamos saber qual a diferença entre
# o peso do peixe que ultrapasse o permitido
excesso = peso_peixe - peso_permitido

taxa = 4.00

# agora, eu não tenho nenhuma saida para eu comparar e ter certeza
# mas, já que a multa é dada por uma taxa de quatro **ao execesso**
# eu julgo que é mais ou menos isso
multa = taxa * excesso

if(peso_peixe > peso_permitido):
	print("Peso do peixe maior do que o permitido")
	print(f"Você terá que pagar {multa}R$ de multa")
