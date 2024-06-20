notas_avaliadas = 50
nota_total = 0

for i in range(0, notas_avaliadas):
	nota_aluno = float(input("Me diga a nota do aluno: "))

	if(nota_aluno < 0 or nota_aluno > 10):
		print("Nota inválida")
	else:
		nota_total = nota_total + nota_aluno

media = nota_total / notas_avaliadas

print("A média foi de", media)
