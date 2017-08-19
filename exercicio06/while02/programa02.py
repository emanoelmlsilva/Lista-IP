cont = 25
soma = 0
while cont > 0:
	num = int(input('Informe um valor: '))
	if(num % 2 == 0 and num > 0):
		soma += 1
	cont -= 1
print('Quantidade de numeros positivos e pares sao {}'.format(soma))
