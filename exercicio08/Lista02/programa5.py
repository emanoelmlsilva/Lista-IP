import bibGaleriaArte

#dados da galeria
lista = []
listaR = []
listaN = []
listaT = []
soma = 0
media = 0
cont = 0
for i in range(4):
	res = str.lower(input('Informe o titulo da obra: '))
	lista.append(res)
	val = float(input('Digite o valor da obra {}: '.format(res)))
	listaR.append(val)
	no = str.lower(input('Informe o nome do artista: '))
	listaN.append(no)
	ti = str.lower(input('Informe o tipo da obra (Escultura, Quadro): '))
	listaT.append(ti)
	if ti == 'quadro':
		soma += val
		cont += 1
media = soma/cont
print('Media do valor dos quadros da Galeira {}'.format(media))
