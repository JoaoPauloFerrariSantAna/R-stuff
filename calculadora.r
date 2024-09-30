calcular <- function(num1, num2, operacao) {
	resultado <- 0

	if(operacao == '+') {
		resultado <- num1 + num2
	}

	if(operacao == '-') {
		resultado <- num1 - num2
	}

	if(operacao == '*') {
		resultado <- num - num2
	}

	if(operacao == '/') {
		resultado <- num1 / num2
	}

	if(operacao == '^') {
		expoente <- as.numeric(readline("Me diga o expoente para elevar o numéro: "))

		resultado <- num1 ^ expoente
	}

	# o professor, na hora da apresentação, tinha perguntado se a gente
	# conseguia tratar números negativos na raiz quadrada...
	# TODO: tratar números negativos
	if(operacao == "sqrt") {
		resultado <- c(sqrt(num1), sqrt(num2))
	}

	return(resultado)
}

numero1		<- as.numeric(readline("Digite um número: "))
numero2		<- as.numeric(readline("Digite um outro número: "))
operacao	<- readline("Me diga a operação (+, -, /, ^, sqrt): ")

calcular(numero1, numero2, operacao)
