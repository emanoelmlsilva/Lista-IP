velocidade = float(input('Informe a velocidade do carro: '))
if(velocidade > 80):
    veloAtual = (velocidade - 80)
    multa = (5 * veloAtual)
    print('Você foi multado por ultrapaçar a velocidade de 80Km/h')
    print('Valor da multa é de {}, velocidade de: {}'.format(multa,velocidade))
else:
    print('Não foi multado')
