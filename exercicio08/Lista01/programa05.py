import testaMultiplo4,testaDivisor
soma=0
cont = 0
div = 300
for i in range(1,4):
	num = int(input('Digite o valor: '))
	m = testaMultiplo4.testaMultiplo4(num)
	if m == True:
		cont+=1
	d = testaDivisor.testaDivisor(div,num)
	if d == True:
		soma += num
print(cont)
print(soma)
