import Abada

v = []
t = []
for i in range(0,5):
	fantQ = int(input('Digite a quantidade de fantasias fendidas: '))
	cc = Abada.calculaComissao(fantQ)
	cb = Abada.calculaBonus(fantQ)
	v.append(cc+cb)
	t.append(fantQ)
for i in range(0,5):
	print('valor total de {} = {:.2f} e os abadares vendidos foram {}'.format(i+1,v[i],t[i]))
