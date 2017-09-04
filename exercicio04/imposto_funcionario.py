salario = float(input('Informe o salario: '))
if(salario > 1000):
    novo_sal = salario * 0.17
else:
    novo_sal = salario * 0.08
print('O valor do imposto que ele ira pagar sera de {}'.format(novo_sal))
