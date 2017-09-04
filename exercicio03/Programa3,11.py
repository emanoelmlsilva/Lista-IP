preçoMerc = float(input('Informe o preço da mercadoria: '))
percent = float(input('Informe o percentual de desconto: '))
desconto = percent*preçoMerc
preçoPagar = preçoMerc-desconto
print('O valor do desconto %4.2f R$'%desconto)
print('O valor a pagar é de %5.2f R$'%preçoPagar)


