x = int(input('Informe a quantidade de peças no estoque: '))
cont = 0
soma = 0
maior = 0
for i in range(1,(x+1)):
	descriçao = input('Descrição: ')
	valor = int(input('Valor: '))
	ano = int(input('Ano: '))
	if(ano < 1827):
		cont += 1
	if(valor > maior):
		maior = valor
		year = ano
		nome = descriçao
	soma += valor
vm =  soma/x
print('Itens produzidos antes de 1827 {} '.format(cont))
print('Valor médio dos itens {:.2f} '.format(vm))
print('Dados dos objetos mais valisos {}, {}'.format(nome,year))
