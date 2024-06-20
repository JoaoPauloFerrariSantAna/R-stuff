print("--------------------------------------")
print("Digite um dos números para votar no candidato: ")
print("45 - Aecio")
print("43 - Marina")
print("13 - Dilma")
print("99 - Voto nulo");
print("Digite '0' para finalizar")
print("--------------------------------------")
	
codigo_dilma 	= 13
codigo_marina	= 43
codigo_aecio 	= 45
codigo_nulo		= 99

total_dilma		= 0
total_aecio		= 0
total_marina	= 0
total_nulo		= 0

codigo_sair = 0
prog_exec = True

while(prog_exec):
	codigo_eleitor = int(input("Digite o código do candidato: "))

	if(codigo_eleitor == codigo_dilma):
		total_dilma = total_dilma + 1

	if(codigo_eleitor == codigo_aecio):
		total_aecio = total_aecio + 1

	if(codigo_eleitor == codigo_marina):
		total_marina = total_marina + 1

	if(codigo_eleitor == codigo_nulo):
		total_nulo = total_nulo + 1

	if(codigo_eleitor == codigo_sair):
		print("Saindo do programa...")
		prog_exec = False

total_votos = total_dilma + total_aecio + total_marina

# para se achar o percentual, tem que dividir
# a parte (o candidato) pelo total (de votos) * 100
# eu vou dividir o total por 100, porque é mais rápido pra mim
percentual_aecio	= total_aecio * (total_votos / 100)
percentual_dilma	= total_dilma * (total_votos / 100)
percentual_marina	= total_marina * (total_votos / 100)

print("--------------------------------------")
print("Estátisticas dos votos (total, nulos):")
print(f"Total de votos: {total_votos}, votos nulos: {total_nulo}.")
print("--------------------------------------")
print("PORCENTAGEM INDIVÍDUAL DOS CANDIDATOS")
print("--------------------------------------")
print("AÉCIO")
print(f"{percentual_aecio}%, votos do candidato: {total_aecio}")
print("--------------------------------------")
print("DILMA")
print(f"{percentual_dilma}%, votos da candidata: {total_dilma}")
print("--------------------------------------")
print("MARINA")
print(f"{percentual_marina}%, votos da candidata: {total_marina}")
print("--------------------------------------")
print("--------------------------------------")

if((percentual_aecio > percentual_dilma) and (percentual_aecio > percentual_marina)):
	print("O candidato Aécio irá ser presidente")
	print("--------------------------------------")
elif((percentual_dilma > percentual_aecio) and (percentual_dilma > percentual_marina)):
	print("A candidata Dilma irá ser presidente")
	print("--------------------------------------")
elif((percentual_marina > percentual_aecio) and (percentual_marina > percentual_dilma)):
	print("A candidata Marina irá ser presidente")
	print("--------------------------------------")
else:
	print("Houve um impasse nesta eleição")
