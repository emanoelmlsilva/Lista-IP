valor_produto = int(input('Informe o valor do produto: '))
tipo = str.lower(input('Informe a forma de pagamento:(Dinheiro / Cheque)'))
if((tipo == 'dinheiro') and (valor_produto >= 100)):
    pagar = (valor_produto - (valor_produto*0.10))
elif((tipo != 'cheque') and (tipo != 'dinheiro')):
    pagar = 'Forma de pagamento invalida'
else:
    pagar = valor_produto
print('R${}'.format(pagar))
    
