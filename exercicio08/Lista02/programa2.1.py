import bibGaleriaArte

#dados da galeria
lista = []
tot = 0
for i in range(60):
        res = str.lower(input('Informe o titulo da obra: '))
        val = float(input('Digite o valor da obra {}: '.format(res)))
        no = str.lower(input('Informe o nome do artista: '))
        ti = str.lower(input('Informe o tipo da obra (Escultura, Quadro): '))
        lista.append([res,val,no,ti])
        if no == 'leonardo resende':
                tot+=val
print('valor total das obras {:.2f}'.format(tot))

