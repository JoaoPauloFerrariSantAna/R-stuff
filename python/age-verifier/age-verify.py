idade = int(input("Me diga a sua idade: "))

if(idade <= 16):
	print("Pode votar")
elif(idade >= 18 and idade < 19):
	print("Pode dirigir")
elif(idade >= 19):
	print("Pode votar e dirigir")
