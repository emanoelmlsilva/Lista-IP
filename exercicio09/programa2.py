
L = []
for i in range(8):
	num = int(input('Digite o {} numero da lista: '.format(i+1)))
	if num % 3 == 0:
		L.append(num)

for i in L:
	print(i,end=' ')
print()

