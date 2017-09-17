import Revistas
lista=[]
listaE=[]
listaC=[]
t = ' '
while True:
	t = str.lower(input('Titulo da revista (fim para encerra lista): '))
	if t == 'fim':
		break
	e = str.lower(input('Nome da editora: '))
	c = float(input('Digite o custo da revista: '))
	lista.append(t)
	listaE.append(e)
	listaC.append(c)

print('================================')
p = str.lower(input('Informe o titulo da Revista para saber a editora: '))
pe = Revistas.pesquisaEditora(lista,p,listaE)
print('Editora da revista {} é {}'.format(p,pe))

print('=================================')
pq = str.lower(input('Informe o titulo para saber a quantidade: '))
cont = Revistas.pesquisaQuantVendas(pq,lista)
print('Quantidade de exemplares vendidos {} '.format(cont))

print('==================================')
pc = str.lower(input('Informe o titulo para saber o custo: '))
custo = Revistas.pesquisaValor(pc,lista,listaC)
print('Custo da revista {} é {:.2f}'.format(pc,custo))

print('=================================')
#quantidade de revista editora globo
conted=0
for i in range(len(lista)):
	if listaE[i] == 'editora globo':
		conted += 1
print('Quantidade de revistas da editora globo {}'.format(conted))

print('=========================================')
#titulo mais vendido
maior=1
v=[]
revista = ' '
for i in lista:
	vend=0
	res=0
	y=0
	l = lista[:]
	x=0
	print('i {}'.format(i))
	while True:
		if i == lista[x]:
			vend+=1
			res+=1
			del (lista[x])
		if len(l)-1 <= 0:
			break
		x += 1
	v.append(res)
	if vend > maior:
		maior = vend
		revista = i
print('Titulo da revista mais vendida {}'.format(revista))

print('=================================')
#media das revistas com mais de 100 exemplares vendidos
soma = 0
x = 0
print('v {}'.format(v))
for i in v:
	if i > 2:
		soma += i
		x +=1
if soma > 0:
	media = soma/x
else:
	media = 0
print('Media das revistas com mais de 100 exemplares vendidos {}'.format(media))
