cont = 1
while(cont <=4):
	num1 = int(input('Informe o primeiro valor: '))
	num2 = int(input('Informe o segundo valor: '))
	if(num1 <= 0 or num2 <= 0):
		print('Você digitou um número inválido')
	else:
		soma = num1 + num2
		mult = num1 * num2
		print('{} {}'.format(soma,mult))
	cont+=1
