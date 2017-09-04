custo_fabrica = float(input('Custo de fabrica: '))
percent_distribu = 0.28
impostos = 0.45
custo_consumidor = (percent_distribu+impostos * custo_fabrica) + custo_fabrica
print('Custo ao consumidor é de %5.2f R$'%custo_consumidor)
