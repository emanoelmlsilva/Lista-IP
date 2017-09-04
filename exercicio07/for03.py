num1 = int(input('Primeiro número -> '))
num2 = int(input('Segundo número -> '))
cont = 0
aux = 0
if(num1 > num2):
	num1,num2 = num2,num1
num1 += 1
for num1 in range(num1,num2):
	if(num1 % 4 == 0):
		cont += 1
print('{} múltiplos'.format(cont))
