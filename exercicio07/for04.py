cont = 0
contm = 0
contb = 0
contbs = 0
conte = 0
soma = 0
tot = 0
med1 = 0
med2 = 0
med3 = 0
val = int(input('Informe a quantidade de vendas: '))
for i in range(val):
	tipo = str.lower(input('Tipo de produto -> '))
	if(tipo == 'movel'):
		med1 +=1
		tot += 1
		cor = str.lower(input('Cor '))
		if(cor == 'marfim'):
			contm += 1
		else:
			contb += 1
	elif(tipo == 'eletrodomestico'):
		med2 += 1
		marca = str.lower(input('Marca '))
		if(marca == 'brastemp'):
			contbs += 1
		else:
			conte += 1
	else:
		med3 += 1
		descriçao = str.lower(input('Descrição -> '))
		preço = float(input('Preço '))
		soma += preço
		cont += 1

if(med1 > 0 and med2 > 0 and med3 > 0):
	print('Percentuais -> {}% marfim, {}% branco'.format((contm/tot)*100,(contb/tot)*100))
	if(contbs == conte):
                print('As duas marcas foram igualmentes vendidas')
	elif(contbs > conte):
                print('Marca mais vendida -> Brastemp')
	else:
		print('Marca mais vendida -> Electrolux')

	md = soma/cont
	print('Preço medio de decoração -> {}'.format(md))

elif(tipo == 'movel'):
	print('Percentuais -> {}% marfim, {}% branco'.format((contm/tot)*100,(contb/tot)*100))
	print('Nenhum eletrodoméstico vendido')
	print('Nenhum objeto de decoração vendido')
elif(tipo == 'eletrodomestico'):
	if(contbs > conte):
		marc = 'Brastemp'
	else:
		marc = 'Electrolux'
	print('Nenhum movel vendido')
	if(contbs == conte):
                print('As duas marcas foram igualmentes vendidas')
#61
	else:
		print('Marca mais vendida -> {}'.format(marc))
	print('Nenhum objeto de decoração vendido')
else:
	md = soma/cont
	print('Nenhum movel foi vendido')
	print('Nenhum eletrodomestico vendido')
	print('Preço medio de decoração -> {}'.format(md))
