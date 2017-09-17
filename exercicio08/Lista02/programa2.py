import bibGaleriaArte

#dados da galeria
lista = []
listaR = []
listaN = []
listaT = []
tot = 0
for i in range(60):
	res = str.lower(input('Informe o titulo da obra: '))
	lista.append(res)
	val = float(input('Digite o valor da obra {}: '.format(res)))
	listaR.append(val)
	no = str.lower(input('Informe o nome do artista: '))
	listaN.append(no)
	ti = str.lower(input('Informe o tipo da obra (Escultura, Quadro): '))
	listaT.append(ti)
	if no == 'leonardo resende':
		tot+=val
print('valor total das obras {:.2f}'.format(tot))
