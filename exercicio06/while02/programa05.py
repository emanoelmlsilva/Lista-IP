cont = 0
while True:
	idade = int(input('Informe a idade: '))
	if(idade >= 3 and idade <= 6):
		cont += 1
	des = str.lower(input('Deseja continuar: '))
	if(des == 'n'):
		break
print('Quantidade total de vacinas aplicadas foram {}'.format(cont))
