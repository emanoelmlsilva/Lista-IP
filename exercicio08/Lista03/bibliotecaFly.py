def calculaValorVoo(destino,turno):
	if turno == 'diurno':
		if destino == 'recife':
			return 100
		elif destino == 'natal':
			return 80
		else:
			return 0
	elif turno == 'noturno':
		if destino == 'fortaleza':
			return 180
		elif destino == 'recife':
			return 90
		else:
			return 0
	else:
		return 0
def validaDadosVoo(destino,turno):
	if turno == 'diurno':
		if destino == 'recife' or destino == 'natal':
			return True
		else:
			return False
	elif turno == 'noturno':
		if destino == 'fortaleza' or destino == 'recife':
			return True
		else:
			return False
	else:
		return False


