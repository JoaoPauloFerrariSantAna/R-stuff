primeiro_num = 0
segundo_num = 1

limite = 12

for n in range(1, limite):
	n_num = primeiro_num + segundo_num
	primeiro_num = segundo_num
	segundo_num = n_num
	print(n_num)
