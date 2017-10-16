nome = input("Informe o seu nome: ")
for i in range(len(nome)):
	for x in range(i+1):
		print(nome[x],end='')
	print()
