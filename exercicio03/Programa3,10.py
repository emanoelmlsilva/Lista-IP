salario = float(input('Entre com o salario: '))
porcentagem = float(input('Informe a porcentagem: '))
aumento = salario * porcentagem
novoSal = aumento + salario
print('Valor do aumento %5.2f R$'%aumento)
print('Valor do novo salario %4.2f R$'%novoSal)
