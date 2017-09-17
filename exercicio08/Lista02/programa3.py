import bibGaleriaArte

#dados da galeria
lista = []
listaR = []
listaN = []
listaT = []
conti = 0
contq = 0
for i in range(50):
	res = str.lower(input('Informe o titulo da obra: '))
	lista.append(res)
	val = float(input('Digite o valor da obra {}: '.format(res)))
	listaR.append(val)
	no = str.lower(input('Informe o nome do artista: '))
	listaN.append(no)
	ti = str.lower(input('Informe o tipo da obra (Escultura, Quadro): '))
	listaT.append(ti)
	if ti == 'escultura':
		conti += 1
	elif ti == 'quadro':
		contq += 1
if conti > contq:
	maior = 'escultura'
else:
	maior = 'quadro'
print('Quantidade maior de {}'.format(maior))
