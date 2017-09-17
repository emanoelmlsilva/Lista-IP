import bibliotecaFly
v = []
tot = 0
cont = 0
for i in range(80):
	sair = True
	while sair:
		dest = str.lower(input('Informe o destino: '))
		tur = str.lower(input('Informe o turno: '))
		vd = bibliotecaFly.validaDadosVoo(dest,tur)
		if vd == True:
			vv = bibliotecaFly.calculaValorVoo(dest,tur)
			v.append(vv)
			if dest == 'recife':
				tot += vv
			elif dest == 'fortaleza':
				cont += 1
			sair = False
		else:
			print('Invalido, digite novamente')
print('Valor de cada passagem vendida {}'.format(v))
print('Valor total pago para passagens para Recife {}'.format(tot))
print('Quantidade de passagens vendidas para Fortaleza {}'.format(cont))
