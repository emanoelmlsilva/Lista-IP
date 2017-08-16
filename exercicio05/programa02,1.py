tipo = str.lower(input('Informe qual o combustivel (Gasolina,Etanol e Diesel: '))
pagar = float(input('Informe a quantidade de litos desejado: '))
if(tipo == 'gasolina'):
    litros = pagar / 2.53
elif(tipo == 'etanol'):
    litros = pagar / 2.09
elif(tipo == 'diesel'):
    litros = pagar / 1.92
if(tipo == 'etanol' and litros > 30):
    print('Litros {:.2f}'.format(litros))
    print('Ganhou troca de óleo')
else:
    print('Litros {:.2f}'.format(litros))
    print('Não ganhou troca de óleo')

