import bibGaleriaArte

#dados da galeria
lista = []
listaR = []
listaN = []
listaT = []
cont=0
for i in range(30):
	res = str.lower(input('Informe o titulo da obra: '))
	lista.append(res)
	val = float(input('Digite o valor da obra {}: '.format(res)))
	listaR.append(val)
	no = str.lower(input('Informe o nome do artista: '))
	listaN.append(no)
	ti = str.lower(input('Informe o tipo da obra (Escultura, Quadro): '))
	listaT.append(ti)
	if no == 'adelia machado' and ti == 'escultura':
		cont += 1

print('Quantidade de escultura de Adelia Machado {}'.format(cont))
