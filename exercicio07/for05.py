contb = 0
contrr = 0
conte = 0
maior = 0
soma = 0
x = int(input('Quantidade de pessoas: '))
for i in range(x):
	idade = int(input('Informe a idade: '))
	opniao = str.lower(input('Informe a opnião: '))
	if(opniao == 'bom'):
		soma += idade
		contb += 1
	if(opniao == 'ruim' or opniao == 'regular'):
		contrr += 1
	if(idade > 30 and opniao == 'excelente'):
		conte += 1
	if(idade > maior):
		maior = idade
print('Media de idade Bom -> {:.0f}'.format(soma/contb))
print('Quantidade respostas Ruim/Regular -> {}'.format(contrr))
print('Pessoas acima de 30 Excelente -> {}'.format(conte))
print('Maior idade -> {}'.format(maior))
