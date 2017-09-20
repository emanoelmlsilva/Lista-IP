import bibGaleriaArte

#dados da galeria
lista = []
conti = 0
contq = 0
for i in range(50):
        res = str.lower(input('Informe o titulo da obra: '))
        val = float(input('Digite o valor da obra {}: '.format(res)))
        no = str.lower(input('Informe o nome do artista: '))
        ti = str.lower(input('Informe o tipo da obra (Escultura, Quadro): '))
        lista.append([res,val,no,ti])
        if ti == 'escultura':
                conti += 1
        elif ti == 'quadro':
                contq += 1
if conti > contq:
        maior = 'escultura'
else:
        maior = 'quadro'
print('Quantidade maior de {}'.format(maior))


