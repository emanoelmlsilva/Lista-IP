cont = 0
soma = 0
v=[]
x=0
quant = int(input('informe a quantidade de peças: '))
for i in range(quant):
	tipo = str.lower(input('Tipo Cobrança: '))
	quantpeça = int(input('Quantidade Peças: '))
	lavagem = str.lower(input('Lavagem a seco: '))
	if(tipo == 'peça' and lavagem == 'sim'):
		tot = quantpeça * 7 + 3.5
		cont += 1
	elif(tipo == 'peça'):
		tot = quantpeça * 7
	elif(tipo == 'peso'and lavagem == 'sim'):
		tot = quantpeça * 5 + 3.5
		cont += 1
	elif(tipo == 'peso'):
		tot = quantpeça * 5
	soma += tot
	v += [tot]
	x+=1
x=0
while x < len(v):
	print('valor do {} pedido -> R$ {}'.format(x+1,v[x]))
	x+=1
print('Total arrecadado {}'.format(soma))
print('Quantidade de lavagens a seco  {}'.format(cont))
