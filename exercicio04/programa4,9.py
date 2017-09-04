valorCasa = float(input('Informe o valor da casa a comprar: '))
salario = float(input('Informe o valor do salario: '))
quantAnosPag = int(input('Informe a quantidade de anos para pagar: '))
if((valorCasa/(quantAnosPag*12)) < (salario*0.3)):
    print('O valor da prestação sera de {:.2f}R$'.format(valorCasa/(quantAnosPag*12)))
else:
    print('O valor da prestação é maior que 30% do salario')
