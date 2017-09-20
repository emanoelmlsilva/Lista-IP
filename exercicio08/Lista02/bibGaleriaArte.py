"""def consultaPreço(titulo,lista,listaR):
	x=0
	for i in lista:
		if titulo == i:
			return listaR[x]
		x+=1


def consultaArtista(titulo,lista,listaN):
	x=0
	for i in lista:
		if titulo == i:
			return listaN[x]
		x+=1

def consultaQuantObras(nome,lista,listaN):
	cont=0
	for i in listaN:
		if nome == i:
			cont+=1
	return cont

def consultaTipo(titulo,lista,listaT):
	x=0
	for i in lista:
		if titulo == i:
			return listaT[x]
		x+=1
"""

def consultaPreço(titulo,lista):
	x=0
	for i in lista:
		if titulo == i[0]:
			return i[1]

def consultaArtista(titulo,lista):
	for i in lista:
		if titulo == i[0]:
			return i[2]

def consultaQuantObras(nome,lista):
	cont=0
	for i in lista:
		if nome == i[2]:
			cont+=1
	return cont

def consultaTipo(titulo,lista):
        for i in lista:
                if titulo == i[0]:
                        return i[3]
