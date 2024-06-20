indice_poluicao = float(input("Me diga indice de poluição: "))

# não foi dito se eu deveria avisar se o valor digitado é inválido ou não
if(indice_poluicao == 0.3):
	print("[AVISO]: Primeiro grupo, por favor paralise as suas atividades")

if(indice_poluicao == 0.4):
	print("[AVISO]: Primeiro e segundo grupo, por favor paralise as suas atividades")

if(indice_poluicao == 0.5):
	print("[AVISO]: Todos os grupos, por favor:")
	print("Parem temporariamente suas atividades")
