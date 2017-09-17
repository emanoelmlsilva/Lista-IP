import bibGaleriaArte

#dados da galeria
lista = []
listaR = []
listaN = []
listaT = []
while True:
	res = str.lower(input('Informe o titulo da obra: '))
	lista.append(res)
	val = float(input('Digite o valor da obra {}: '.format(res)))
	listaR.append(val)
	no = str.lower(input('Informe o nome do artista: '))
	listaN.append(no)
	ti = str.lower(input('Informe o tipo da obra (Escultura, Quadro): '))
	listaT.append(ti)
	cont = input('Deseja para (S/n): ')
	str.lower(cont)
	if cont == 'n':
		break

print('==============Escolha==========')
print('1 para Consulta de preço\n2 para Consulta de Artista\n3 para Consulta da quantidade de obras\n4 para Consulta de tipo')
escolha = int(input('=> ')) #str.lower(input('=> '))
if escolha == 1: #'consulta de preço':
	t = str.lower(input('Informe o titulo da obra: '))
	cp = bibGaleriaArte.consultaPreço(t,lista,listaR)
	print('Valor da Obra {:.2f} R$'.format(cp))
elif escolha == 2: #'consulta de artista':
	t = str.lower(input('Informe o nome da obra: '))
	ca = bibGaleriaArte.consultaArtista(t,lista,listaN)
	print('Nome do Artista: {}'.format(ca))
elif escolha == 3: #'consulta da quantidade de obras':
	a = str.lower(input('Informe o nome do artista: '))
	cqo = bibGaleriaArte.consultaQuantObras(a,lista,listaN)
	print('Quantidade de Obras na Galeria: {}'.format(cqo))
elif escolha == 4: #'consulta de tipo':
	t = str.lower(input('Informe o titulo da obra: '))
	ct = bibGaleriaArte.consultaTipo(t,lista,listaT)
	print('O tipo da Obra é {}'.format(listaT))
else:
	print('Invalido, tente novamente')
