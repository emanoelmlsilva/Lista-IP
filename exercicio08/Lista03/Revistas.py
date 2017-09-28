def pesquisaEditora(lista,titulo):
	for x,i in enumerate(lista):
		if titulo == i[0]:
			return i[1]

def pesquisaQuantVendas(titulo,lista):
	quantV=0
	for x,i in enumerate(lista):
		if titulo == i[0]:
			quantV+=1
	return quantV

def pesquisaValor(titulo,lista):
	for x,i in enumerate(lista):
		if titulo == i[0]:
			return i[2]
	return None

