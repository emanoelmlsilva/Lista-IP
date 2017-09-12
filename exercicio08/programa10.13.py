import bibliotecacorreios
quant = 0
soma = 0
pesoTotal = list(range(3))

for i in range(3):
	tipo = str.lower(input('informe o tipo do item (documento ou pacote): '))

	peso = float(input('Digite o peso em quilo: '))

	embalagem = str.lower(input('Informe  o tipo da embalagem (grande, pequena, media): '))

	entrega = str.lower(input('Informe o tipo da entrega(normal,sedex,sedex10): '))

	bibliotecacorreios.validaEntrega(entrega)
	e = bibliotecacorreios.calcularCustoEntrega(entrega)
	if e == 8:
		quant += 1

	bibliotecacorreios.validaPeso(peso)
	pesoConv = bibliotecacorreios.convertePeso(peso)
	pesoTotal[i] += pesoConv

	bibliotecacorreios.tipoItem(tipo)
	i = bibliotecacorreios.calculaCustoItem(tipo, pesoConv)


	bibliotecacorreios.validaEmbalagem(embalagem)
	b = bibliotecacorreios.calculaCustoEmbalagem(embalagem)

	soma += e+i+b

print('Custo total {:.2f} R$'.format(soma))
print('Quantidade de entregas com sedex10 {}'.format(quant))

for i in range(3):
	print('peso em gramas {:.2f} g'.format(pesoTotal[i]))
