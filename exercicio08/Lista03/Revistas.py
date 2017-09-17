def pesquisaEditora(lista,titulo,listaE):
	x=0
	for i in lista:
		if titulo == i:
			return listaE[x]
		x+=1

def pesquisaQuantVendas(titulo,lista):
	quantV=0
	for i in lista:
		if titulo == i:
			quantV+=1
	return quantV

def pesquisaValor(titulo,lista,listaC):
	x=0
	for i in lista:
		if titulo == i:
			return listaC[x]
		x+=1
	return 0

