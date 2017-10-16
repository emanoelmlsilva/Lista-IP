nome = input("informe o seu nome: ")
for i in range(len(nome)-1,-1,-1):
	for x in range(i+1):
		print(nome[x],end='')
	print()
