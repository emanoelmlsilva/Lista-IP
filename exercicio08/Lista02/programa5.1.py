import bibGaleriaArte

#dados da galeria
lista = []
soma = 0
media = 0
cont = 0
for i in range(4):
        res = str.lower(input('Informe o titulo da obra: '))
        val = float(input('Digite o valor da obra {}: '.format(res)))
        no = str.lower(input('Informe o nome do artista: '))
        ti = str.lower(input('Informe o tipo da obra (Escultura, Quadro): '))
        lista.append([res,val,no,ti])
        if ti == 'quadro':
                soma += val
                cont += 1
media = soma/cont
print('Media do valor dos quadros da Galeira {}'.format(media))



