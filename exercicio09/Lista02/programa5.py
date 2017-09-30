lista = []
for i in range(100):
	nome = str(input("Informe o nome do animal: "))
	idade = float(input("Digite a idade do animal: "))
	tipo = str(input("Informe o tipo do animal: "))
#	lista.extend([nome,idade,tipo]) #extend adiciona tudo em uma so lista
	lista.append([nome,idade,tipo]) #append adiciona lista dentro de lista
print(lista)
