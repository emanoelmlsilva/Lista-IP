num1 = float(input('Digite o primeiro valor: '))
num2 = float(input('Digite o segundo valor: '))
num3 = float(input('Digite o terceiro valor: '))
if((num1>num2)and(num1>num3)):
    valor = num1
elif((num2>num1)and(num2>num3)):
    valor = num2
else:
    valor = num3
print('O maior valor é o {}'.format(valor))
