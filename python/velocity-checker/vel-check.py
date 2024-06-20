vel_max		= int(input("Me diga a velocidade da pista: "))
vel_atual	= int(input("Me diga a sua velocidade atual: "))
vel_dif		= vel_atual - vel_max

if(vel_atual > vel_max):
	print(f"Você está {vel_dif} quilometros acima do limite de velocidade")
else:
	print("Você está dentro da velocidade permitida");

