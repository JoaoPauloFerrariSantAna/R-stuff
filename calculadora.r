calcular <- function(num1, num2, operacao) {
	resultado <- 0

	if(operacao == '+') {
		resultado <- num1 + num2
	}

	if(operacao == '-') {
		resultado <- num1 - num2
	}

	if(operacao == '/') {
		resultado <- num1 / num2
	}

	if(operacao == '^') {
		expoente <- as.numeric(readline("Me diga o expoente para elevar o numéro: "))

		resultado <- num1 ^ expoente
	}

	# eu não vou conseguir retornar as raizes dos dois números
	if(operacao == "sqrt") {
		resultado <- sqrt(num1)
	}

	return(resultado)
}


numero1		<- as.numeric(readline("Digite um número: "))
numero2		<- as.numeric(readline("Digite um outro número: "))
operacao	<- readline("Me diga a operação (+, -, /, ^, sqrt): ")

print(calcular(numero1, numero2, operacao))
