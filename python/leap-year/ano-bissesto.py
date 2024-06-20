ano_atual = int(input("Qual o ano atual? ")) 

for i in range(1, ano_atual):
	# quando um número for multiplo de outro,
	# o resto da divisão sempre vai ser 0
	if((i % 400 == 0) or ((i % 4 == 0) and (i % 100 != 0))):
		print(i)
