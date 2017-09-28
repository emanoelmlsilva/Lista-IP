import Revistas
lista=[]
while True:
	t = str.lower(input('Titulo da revista (fim para encerra lista): '))
	if t == 'fim':
		break
	e = str.lower(input('Nome da editora: '))
	c = float(input('Digite o custo da revista: '))
	lista.append([t,e,c])
print('================================')
p = str.lower(input('Informe o titulo da Revista para saber a editora: '))
pe = Revistas.pesquisaEditora(lista,p)
print('Editora da revista {} é {}'.format(p,pe))

print('=================================')
pq = str.lower(input('Informe o titulo para saber a quantidade: '))
cont = Revistas.pesquisaQuantVendas(pq,lista)
print('Quantidade de exemplares vendidos {} '.format(cont))

print('==================================')
pc = str.lower(input('Informe o titulo para saber o custo: '))
custo = Revistas.pesquisaValor(pc,lista)
print('Custo da revista {} é {:.2f}'.format(pc,custo))

print('=================================')
#quantidade de revista editora globo
conted=0
for x,i in enumerate(lista):
	if i[1] == 'globo':
		conted += 1
print('Quantidade de revistas da editora globo {}'.format(conted))

print('=========================================')
#titulo mais vendido
maior=0 #1
v=[]
revista = None
cont=0
lQuant=[]
for x,i in enumerate(lista):
	vend=0
	res=0
	l=lista[:]
	for y,c in enumerate(l):
		if i[0] == c[0]:
			vend+=1
			res+=1
			lista.remove(c)
	if res >= 2: #contagem das revistas com mais de 100 exemplares
		v.append(res)
		lQuant.append(i[2])
		cont+=1
	if vend > maior:
		maior = vend
		revista = i[0]
print('Titulo da revista mais vendida {}'.format(revista))

print('=================================')
#media das revistas com mais de 100 exemplares vendidos
soma = 0
for i in lQuant: #soma das revistas com mais de 100 exemplares
	soma += i
if soma > 0:
	media = soma/cont
else:
	media = 0
print('Media das revistas com mais de 100 exemplares vendidos {}'.format(media))

