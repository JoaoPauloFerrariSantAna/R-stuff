gost_masc = 0
gost_femi = 0

nao_gost_masc = 0
nao_gost_femi = 0

pessoas_intre = 2000

i = 0

while(i <= pessoas_intre):
	sexo		= str(input("Qual o seu sexo? (m/f) "))
	gost_prod	= str(input("Você gostou do produto? (s/n) "))

	if(gost_prod == 's'):
		if(sexo == 'm'):
			gost_masc = gost_masc + 1

		if(sexo == 'f'):
			gost_femi = gost_femi + 1
	else:
		if(sexo == 'm'):
			nao_gost_masc = nao_gost_masc + 1

		if(sexo == 'f'):
			nao_gost_femi = nao_gost_femi + 1

	i = i + 1

gost_total		= gost_masc + gost_femi
nao_gost_total	= nao_gost_masc + nao_gost_femi

print(f"Um total de {gost_masc} homens gostaram do produto")
print(f"Um total de {nao_gost_masc} homens não gostaram do produto")
print(f"Um total de {gost_femi} mulheres gostaram do produto")
print(f"Um total de {nao_gost_femi} mulheres não gostaram do produto")
print(f"Total de pessoas que gostaram do produto: {gost_total}")
print(f"Total de pessoas que não gostaram do produto: {nao_gost_total}")

if(nao_gost_total > gost_total):
	print("Não vale apena lançar o produto")
else:
	print("Vale apena lançar o produto")
