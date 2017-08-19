num = 0
soma = 0
cont = 0
while num >= 0:
	if(num > 0):
		soma += num
		cont += 1
	num = int(input('Informe a quantidade de filhos: '))
med = soma / cont
print('Media de filhos {}'.format(med))
