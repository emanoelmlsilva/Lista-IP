v = []
L = []
for i in range(5):
	v.append(int(input('Digite o {} numero da lista: '.format(i+1))))

for x in range(len(v)-1):
	L.append(v[x]+v[x+1])
L.append(v[-1])
print('lista {}'.format(v))
print('lista somada {}'.format(L))
