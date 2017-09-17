def calculaComissao(quant):
	valor = quant * 5.6
	return valor

def calculaBonus(quantb):
	if quantb>50:
		taxa = 70
	else:
		taxa = 0
	return taxa
