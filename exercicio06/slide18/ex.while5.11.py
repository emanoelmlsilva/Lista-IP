"""Escreva um programa que pergunte o depósito inicial e a taxa de juros de uma poupança.Exiba os
valores mês a mês para os 24 primeiros meses.Escreva o total ganho com juros no periodo"""

depo = float(input('Informe o valor do depósito inicial: '))
taxa = float(input('Informe a taxa de juros da poupança: '))
cont = 1
res = depo
"""
saldo = depo
while cont <= 24:
    res += (taxa/100)*depo
    depo = res
    cont += 1
    print('%d mes = %3.2f' % (cont, res))
soma = res - saldo
print('total de juros ganho no periodo: %3.2f'%soma)
 ou"""
dep = 0
while cont <= 24:
    res = (taxa/100)*depo
    depo += res
    dep += res
    print('%d mes = %3.2f' % (cont, depo))
    cont += 1
print('total de juros ganho no periodo: %3.2f'%(dep))
