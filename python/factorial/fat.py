print("Programa para calcular o fatorial de um número")

fatorial = 1
numero = int(input("Digite um número: "))


# Decreasing with range: http://tiny.cc/h9iuxz
for i in range(numero, 1, -1):
	fatorial = fatorial * i

print("O fatorial de", numero, "é", fatorial)
