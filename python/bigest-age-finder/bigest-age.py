# cade as questões "11" e "12", professor?

prog_exec = True

print("Digite '0' para sair")

maior_idade = 0

while(prog_exec):
	idade_pessoa1 = int(input("Idade da pessoa? "))
	idade_pessoa2 = int(input("Idade da outra pessoa? "))

	if(idade_pessoa1 > idade_pessoa2):
		maior_idade = idade_pessoa1
	else:
		maior_idade = idade_pessoa2
		print("A maior idade deste par é", maior_idade)

	if(idade_pessoa1 == 0 or idade_pessoa2 == 0):
		print("Saindo do programa...")
		prog_exec = False
