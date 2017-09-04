quant_kwh = float(input('Informe a quantidade de kWh consumido: '))
print('R para residências\n')
print('I para indústrias\n')
print('C para comércios\n')
tipo = str.lower(input('Tipo da instalação: '))
if(tipo == 'r'):
    if(quant_kwh <= 500):
        preco = quant_kwh * 0.40
    else:
        preco = quant_kwh * 0.65
elif(tipo == 'c'):
    if(quant_kwh <= 1000):
        preco = quant_kwh * 0.55
    else:
        preco = quant_kwh * 0.60
elif(tipo == 'i'):
    if(quant_kwh <= 5000):
        preco = quant_kwh * 0.55
    else:
        preco = quant_kwh * 0.60
print('O valor a pagar pelo fornecimento de energia elétrica é {} R$'.format(preco))


