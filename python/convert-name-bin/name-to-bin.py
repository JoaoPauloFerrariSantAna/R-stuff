import re

def remove_ob_prefix(binary):
	return re.sub(r"0b", '', binary)

def parse_name_to_int(name):
	ascii_list = []

	for i in range(0, len(name)):
		ascii_list.append(ord(name[i]))

	return ascii_list

def parse_int_to_bin(name_int):
	name_binary = []

	for j in range(0, len(name_int)):
		name_binary.append(bin(name_int[j]))
	
	return name_binary

def show_name_bin(name_bin):
	print("Your name in binary is: ", end='')

	for k in range(0, len(name_bin)):
		print(remove_ob_prefix(name_bin[k]), end=' ')
	
	print(end='\n')
	
name = str(input("Tell me your name: "))
name_converted = parse_name_to_int(name)
name_binary = parse_int_to_bin(name_converted)

show_name_bin(name_binary)
