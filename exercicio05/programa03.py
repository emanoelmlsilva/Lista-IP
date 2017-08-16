num1 = int(input('Digite o primeiro número: '))
num2 = int(input('Digite o segundo número; '))
num3 = int(input('Digite o terceiro número: '))

if((num1 > num2) and (num1 > num3)):
    saida = num1
elif((num2 > num1) and (num2 > num3)):
    saida = num2
else:
    saida = num3
print('O maior número é {}'.format(saida))
