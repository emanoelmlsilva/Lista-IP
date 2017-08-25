"""Escreva um programa que pergunte o valor inicial de uma divida e o juro mensal.Pergunte o valor que
também será pago.Emprima o número de meses para que a divida seja paga, o total de juros pago."""

valor_inicial = float(input('Informe o valor inicial: '))
juros_mensal = float(input('Informe o valor do juros mensal: '))
pagar_mensal = float(input('Informe o valor mensal pago: '))
mes = 0
if(juros_mensal/100 > pagar_mensal):
    print('Não poderar ocorrer o pagamento devido ao juros maior que o pagamento mensal')
else:
    saldo = valor_inicial
    juros = 0
    while(saldo <= 0):
        mensal = (juros_mensal/100) * saldo
        saldo += mensal - pagar_mensal
        juros += mensal
        tot = valor_inicial+juros
        print('Saldo da divida do mes %d é de %5.2f'%(mes,saldo))
        mes += 1
print('Total de meses para pagar a divida %d'%mes)
print('Total pago com juros: %5.2f'%tot)
print('Total de juros pago: %5.2f'%juros)
"""
if juros_mensal/100 > pagar_mensal:
    print('Não podera pagar porque o juros mensal é maior que o pagamento mensal')
else:
    saldo = valor_inicial
    j = 0
    while saldo > pagar_mensal:
        pago = saldo*(juros_mensal/100)
        saldo = saldo + pago - pagar_mensal
        j += pago
        print('Saldo da divida no mes de %d é de R$ %5.3f.'%(mes,saldo))
        mes += 1
print('números de meses para que a divida seja paga ',mes-1)
print('Total pago: %5.3f'%saldo)
print('Total de juros pago: %4.2f'%j)"""