def calculaCondominio(string,valor):
	if string == 'duna':
		valor = (300 * (0.02*valor)) + 300
	elif string == 'chateau':
		valor = (450 * (0.04*valor)) + 450
	elif string == 'petit':
		valor = (220 * (0.03*valor)) + 220
	else:
		valor = 'invalido'
	return valor

abc = str.lower(input('Digite o nome do edificio: '))
valor = int(input('Digite a quantidade de dias de atraso no pagamento: '))

resp = calculaCondominio(abc,valor)

print(resp)
