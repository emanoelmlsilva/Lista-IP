cont = 50
soma = 0
while cont > 0:
	num = int(input('Informe o valor: '))
	if(num % 3 == 0):
		soma += 1
	cont -= 1
print('A soma dos numeros que sao multiplos de 3 sao {}'.format(soma))
