num = 1
soma = 0
cont = 0
while num != 100:
	if(num % 2 == 0):
		soma += num
		cont += 1
	num = int(input('Informe o valor: '))
if(cont == 0):
	print('nao foram lidos numeros pares')
else:
	resul = int(soma / cont)
	print('Media: {}'.format(resul))
