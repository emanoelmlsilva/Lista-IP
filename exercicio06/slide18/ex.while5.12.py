""" Altere o programa anterior de forma a perguntar também o valor depositado mensalmete.Essa valor
será depositado no inicio de cada mês, e você deve concideŕa-lo para o cálculo de juros do mês seguinte.
"""
depo = float(input('Informe o valor do depósito inicial: '))
taxa = float(input('Informe a taxa de juros da poupança: '))
depo_mensal = float(input('Informe o valor depositado ao mes: '))
cont = 0
res = depo
saldo = depo
while cont < 24:
    cont += 1
    res += (taxa/100)*depo+depo_mensal
    depo = res
    print('%d mes = %3.2f' % (cont, res))
soma = res - saldo
print('total de juros ganho no periodo: %3.2f'%soma)