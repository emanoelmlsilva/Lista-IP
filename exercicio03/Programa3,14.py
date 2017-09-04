km_percorrido = float(input('Informe a quantidade de Km precorrido: '))
dias_alugado = int(input('Informe a quantidade de dias que o carro passou alugado: '))
preço_pagar = km_percorrido*0.15 + dias_alugado*60
print('A preço do alugel do carro é de %5.2f R$'%preço_pagar)
