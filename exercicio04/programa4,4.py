salario = float(input('Informe o salario do funcionario: '))
if(salario > 1250):
    salSuper = salario + (salario*(10/100))
else:
    salSuper = salario + (salario*(15/100))
print('Salario com aumento é de {}'.format(salSuper))
