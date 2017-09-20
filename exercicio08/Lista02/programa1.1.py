from bibGaleriaArte import consultaPreço,consultaArtista,consultaQuantObras,consultaTipo

#dados da galeria
lista = []
while True:
        res = str.lower(input('Informe o titulo da obra: '))
        val = float(input('Digite o valor da obra {}: '.format(res)))
        no = str.lower(input('Informe o nome do artista: '))
        ti = str.lower(input('Informe o tipo da obra (Escultura, Quadro): '))
        lista.append([res,val,no,ti])
        cont = input('Deseja para (S/n): ')
        str.lower(cont)
        if cont == 'n':
                break
print(lista)

print('==============Escolha==========')
print('1 para Consulta de preço\n2 para Consulta de Artista\n3 para Consulta da quantidade de obras\n4 para Consulta de tipo')
escolha = int(input('=> ')) #str.lower(input('=> '))
if escolha == 1: #'consulta de preço':
	t = str.lower(input('Informe o titulo da obra: '))
	cp = consultaPreço(t,lista)
	print('Valor da Obra {:.2f} R$'.format(cp))
elif escolha == 2: #'consulta de artista':
        t = str.lower(input('Informe o nome da obra: '))
        ca = consultaArtista(t,lista)
        print('Nome do Artista: {}'.format(ca))
elif escolha == 3: #'consulta da quantidade de obras':
        a = str.lower(input('Informe o nome do artista: '))
        cqo = consultaQuantObras(a,lista)
        print('Quantidade de Obras na Galeria: {}'.format(cqo))
elif escolha == 4: #'consulta de tipo':
        t = str.lower(input('Informe o titulo da obra: '))
        ct = consultaTipo(t,lista)
        print('O tipo da Obra é {}'.format(ct))
else:
        print('Invalido, tente novamente')






