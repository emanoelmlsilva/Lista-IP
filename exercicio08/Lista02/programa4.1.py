import bibGaleriaArte

#dados da galeria
lista = []
cont=0
for i in range(30):
        res = str.lower(input('Informe o titulo da obra: '))
        val = float(input('Digite o valor da obra {}: '.format(res)))
        no = str.lower(input('Informe o nome do artista: '))
        ti = str.lower(input('Informe o tipo da obra (Escultura, Quadro): '))
        if no == 'adelia machado' and ti == 'escultura':
                cont += 1

print('Quantidade de escultura de Adelia Machado {}'.format(cont))


