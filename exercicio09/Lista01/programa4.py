n = []
for i in range(5):
	n.append(float(input('Digite a {} nota: '.format(i+1))))
cont=0
for x in n:
	if x > 8:
		cont +=1 
print('Quantidade de notas acima de 8: {}'.format(cont))
