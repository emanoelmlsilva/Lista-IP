N = int(input())
lista = [6,2,5,5,4,5,6,3,7,6]
for i in range(N):
	soma = 0
	V = input()
	for x in V:
		soma += lista[int(x)]
	print("{} ".format(soma))
