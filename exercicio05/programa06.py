valor_produto = int(input('Informe o valor do produto: '))
tipo = str.lower(input('Informe a forma de pagamento:(Dinheiro / Cheque ou Cartao)'))
if((tipo == 'dinheiro') and (valor_produto >= 100)):
    pagar = (valor_produto - (valor_produto*0.10))
elif((tipo != 'cheque') and (tipo != 'dinheiro') and (tipo != 'cartao')):
    pagar = 'Forma de pagamento invalida'
elif(tipo == 'cartao'):
    escolha = str.lower(input('Debito ou Credito:'))
    if(escolha == 'debito'):
        pagar = valor_produto
    elif(escolha == 'credito'):
        quant = int(input('Informe a quantidade de parcelas (maxi = 3):'))
        pagar = valor_produto/quant
    else:
        print('Opçao nao existe')
else:
    pagar = valor_produto
if(tipo == 'cartao'):
    print('R$ {}'.format(valor_produto))
    print('{} parcelas de R$ {}'.format(quant,pagar))
else:
    print('R$ {}'.format(pagar))
    
