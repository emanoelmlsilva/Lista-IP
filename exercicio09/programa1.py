v = []
for x in range(5):
	v.append(int(input('Digite o {} numero: '.format(x+1))))

menor = v[0]
for i in v:
	if i < menor:
		menor = i

print('O menor numero da lista é {}'.format(menor))
