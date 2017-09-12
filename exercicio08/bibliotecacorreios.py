Documento = 'documento'
Pacote = 'pacote'
Pequena = 'pequena'
Media = 'media'
Grande = 'grande'
Normal = 'normal'
Sedex = 'sedex'
Sedex10 = 'sedex10'

def tipoItem(tipo):
	if tipo == Pacote or tipo == Documento:
		return True
	else:
		return False

def validaPeso(peso):
	if peso >= 0:
		return True
	else:
		return False

def convertePeso(peso):
	peso *= 1000
	return peso

def calculaCustoItem(tipo ,  peso):
	if tipo == Documento:
		x = (2 * peso) / 1000
	else:
		x = (3 * peso) / 1000
	return x

def validaEmbalagem(embalagem):
	if embalagem == Pequena or embalagem == Media or embalagem == Grande :
		return True
	else:
		return False

def calculaCustoEmbalagem(embalagem):
	if embalagem == Pequena:
		custEmb = 4
	elif embalagem == Media:
		custEmb = 7
	elif embalagem == Grande:
		custEmb = 10
	else:
		custEmb = 0
	return custEmb

def validaEntrega(entrega):
	if entrega == Normal or entrega == Sedex or entrega == Sedex10:
		return True
	else:
		return False

def calcularCustoEntrega(entrega):
	if entrega == Normal:
		custEnt = 0
	elif entrega == Sedex:
		custEnt = 5
	elif entrega == Sedex10:
		custEnt = 8
	return custEnt
