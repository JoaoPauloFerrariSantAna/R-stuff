numero = int(input("Digite um número com três casa decimais: "))

centena = numero // 100
dezena	= (numero % 100) // 10
unidade = numero % 10

print(f"Centena = {centena}, dezena = {dezena}, unidade = {unidade}")
