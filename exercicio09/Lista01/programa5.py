n = []
for i in range(4):
	n.append(int(input('Informe a quantidade de alunos da {} turma: '.format(i+1))))
soma=0
for x in n:
	soma += x
print('Quantidade de alunos é {}'.format(soma))
